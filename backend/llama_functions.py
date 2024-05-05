def get_procedure_name(model, tokenizer, med, guide):
    pass

def get_cpt_codes(model, tokenizer, med, guide):
    pass

def get_summary(model, tokenizer, med, guide):
    messages = [
    {"role": "system", "content": "You are a medical copilot assistant. You will be given a medical record and you need to summarize it. Nothing more, nothing less."},
    {"role": "user", "content": "{med}"},
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

def get_steps(model, tokenizer, med, guide):
    pass