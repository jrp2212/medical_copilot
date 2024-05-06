from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch
import os
import re

def load_model(model_name: str, model_dir: str):
    global model, tokenizer
    if not os.path.exists(model_dir):
        print("Directory Not Found")
        os.makedirs(model_dir, exist_ok=True)
    
    try:
        model = AutoModel.from_pretrained(model_dir)
        print("Model loaded from local directory.")
    except Exception as e:
        print("Model not found locally, downlding from Hugging Face.")
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            load_in_8bit=True,
            device_map="auto",
        )

        model.save_pretrained(model_dir)
        print("Model downloaded and saved locally.")
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)

def unload_model():
    global model
    if model:
        del model
        torch.cuda.empty_cache()
        print("Model and cache cleared.")

def get_procedure_name(med, guide):
    pass


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

def get_steps(med, guide):
    pass