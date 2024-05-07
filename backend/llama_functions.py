from transformers import AutoModel, AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch
import os
import re
from fuzzywuzzy import process

def load_model(model_name: str, model_dir: str):
    global model, tokenizer
    if not os.path.exists(model_dir):
        print("Model Not Found, Downloading From HuggingFace...")
        os.makedirs(model_dir, exist_ok=True)

        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            load_in_8bit=True,
            device_map="auto",
        )
        model.save_pretrained(model_dir)
        print("Model Saved")
    else:
        print("Saved Model Found, Loading Up...")

        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            load_in_8bit=True,
            device_map="auto",
        )
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)


def unload_model():
    global model
    if model:
        del model
        torch.cuda.empty_cache()
        print("Model and cache cleared.")

def get_procedure_name(med, guide):
    
    messages = [
    {"role": "system", "content": "You are a medical copilot assistant. You will be given a patient intake form that contains guidelines for a procedure. Please print out just the procedure name. Nothing more, nothing less."},
    {"role": "user", "content": f"{guide}"},
    ]

    input_ids = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        return_tensors="pt"
    ).to(model.device)

    terminators = [
        tokenizer.eos_token_id,
        tokenizer.convert_tokens_to_ids("<|eot_id|>")
    ]

    outputs = model.generate(
        input_ids,
        max_new_tokens=256,
        eos_token_id=terminators,
        do_sample=True,
        temperature=0.6,
        top_p=0.9,
    )
    response = outputs[0][input_ids.shape[-1]:]
    return tokenizer.decode(response, skip_special_tokens=True)


def get_cpt_codes(med, guide):
    messages = [
    {"role": "system", "content": """You are a medical copilot assistant. You will be given a patient intake form that contains guidelines for a procedure. Please find the CPT Codes, nothing more, nothing less. Example output looks like: [
        "63430",
        "12232",
        "32423",
        "23412",
        "89454",
        "64495"
    ]"""},
    {"role": "user", "content": f"{guide}"},
    ]

    input_ids = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        return_tensors="pt"
    ).to(model.device)

    terminators = [
        tokenizer.eos_token_id,
        tokenizer.convert_tokens_to_ids("<|eot_id|>")
    ]

    outputs = model.generate(
        input_ids,
        max_new_tokens=256,
        eos_token_id=terminators,
        do_sample=True,
        temperature=0.6,
        top_p=0.9,
    )
    output = outputs[0][input_ids.shape[-1]:]
    response = tokenizer.decode(output, skip_special_tokens=True)

    codes_part = response.split("[")[1].split("]")[0]
    cpt_codes_list = [code.strip(' "') for code in codes_part.split(",")]
    return cpt_codes_list



def get_summary(med, guide):
    messages = [
    {"role": "system", "content": "You are a medical copilot assistant. You will be given a medical record and you need to summarize it. Nothing more, nothing less."},
    {"role": "user", "content": f"{med}"},
    ]

    input_ids = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        return_tensors="pt"
    ).to(model.device)

    terminators = [
        tokenizer.eos_token_id,
        tokenizer.convert_tokens_to_ids("<|eot_id|>")
    ]

    outputs = model.generate(
        input_ids,
        max_new_tokens=256,
        eos_token_id=terminators,
        do_sample=True,
        temperature=0.6,
        top_p=0.9,
    )
    response = outputs[0][input_ids.shape[-1]:]
    return tokenizer.decode(response, skip_special_tokens=True)

def get_steps(med, guide, key):
    # modified code to only work on one question, but can be scaled to work on all questions

    first_question, options = extract_question(guide, key)

    messages = [
    {"role": "system", "content": """You are a medical copilot assistant. You will be given a medical record, guideline document, and a question along with options from the guideline document. Please select the appropriate option and provide reasoning for your selection. Output should be in the following format: {selected_option: "Option A", reasoning: "Because..."""},
    
    {"role": "user", "content": f"Question: {first_question}\nOptions: {options}\n\nGuideline Document: {guide}\n\nMedical Record: {med}"},
    ]

    # Generate the model's response
    input_ids = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        return_tensors="pt"
    ).to(model.device)

    terminators = [
        tokenizer.eos_token_id,
        tokenizer.convert_tokens_to_ids("<|eot_id|>")
    ]

    outputs = model.generate(
        input_ids,
        max_new_tokens=256,
        eos_token_id=terminators,
        do_sample=True,
        temperature=0.6,
        top_p=0.9,
    )
    response = outputs[0][input_ids.shape[-1]:]
    answer = tokenizer.decode(response, skip_special_tokens=True)

    selected_option, reasoning = extract_option_and_reasoning(answer, options)

    return {"key": str(key), "question": first_question, "options": construct_options_structure(selected_option, options), "reasoning": reasoning}


def extract_question(guide, question_number):
    # Split the guide into lines
    lines = guide.split("\n")

    # Create a pattern to match question lines starting with the specific question number
    question_pattern = re.compile(rf"^{question_number}\.")

    # Find the line with the specified question
    question_line_index = next((i for i, line in enumerate(lines) if question_pattern.match(line)), None)
    if question_line_index is None:
        return None  # Return None if the question number does not exist

    # Extract the question
    question = lines[question_line_index].split(" ", 1)[1]

    # Extract the options
    options = []
    for line in lines[question_line_index+1:]:
        if re.match(r"[A-Z]\)", line):
            options.append(line.split(" ", 1)[1])
        else:
            break

    return question, options

def extract_option_and_reasoning(answer, options):
    # Extract the selected option
    selected_option = None
    highest_ratio = 0
    for option in options:
        ratio = process.extractOne(option, [answer])[1]
        if ratio > highest_ratio:
            highest_ratio = ratio
            selected_option = option

    # Extract the reasoning
    reasoning_start = answer.index("Reasoning: ") + len("Reasoning: ")
    reasoning = answer[reasoning_start:]

    return selected_option, reasoning

def construct_options_structure(selected_option, options):
    # Initialize the options structure
    options_structure = []

    # Assign keys to the options
    keys = [str(i * 10) for i in range(1, len(options) + 1)]

    # Construct the options structure
    for key, option in zip(keys, options):
        options_structure.append({
            "key": key,
            "text": option,
            "selected": option == selected_option
        })

    return options_structure