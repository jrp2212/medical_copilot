from typing import List, Optional
from uuid import uuid4
from time import time
import json
import llama_functions as llama

def gen_case_id():
    return "case_" + str(uuid4()).split("-")[0]

class Case:
    def __init__(self, payload):
        """ constuctor. assigns a unique case_id """
        self.med = payload.get('medText', '')  
        self.guide = payload.get('guideText', '') 

        self.case_id = gen_case_id()
        self.created_at = time()
        self.status = "submitted"
        self.procedure_name = ""
        self.cpt_codes = []
        self.summary = ""
        self.steps = []

        self.progress = 0 

    def to_json(self):
        """Select JSON file based on the progress."""
        file_paths = ["../assets/response.json", "../assets/response-1.json", "../assets/response-2.json", "../assets/response-3.json"]
        status = ["started", "processing", "processing", "complete"]

        index = min(self.progress, len(file_paths) - 1)
        self.status = status[index]

        if index == 1:
            self.procedure_name = llama.get_procedure_name(self.med, self.guide)
            self.cpt_codes = llama.get_cpt_codes(self.med, self.guide)
        
        if index == 2:
            self.summary = llama.get_summary(self.med, self.guide)
        
        file_path = file_paths[index]
        try:
            with open(file_path, 'r') as file:
                json_data = json.load(file)
                json_data["case_id"] = self.case_id
                json_data["status"] = self.status
                json_data["created"] = self.created_at
                json_data["procedure_name"] = self.procedure_name
                json_data["cpt_codes"] = self.cpt_codes
                json_data["summary"] = self.summary
            
                if index == 3:
                    generated_step = llama.get_steps(self.med, self.guide, 0)
                    print(generated_step)
                    for step in json_data["steps"]:
                        if step["key"] == generated_step["key"]:
                            step.update(generated_step)

                    # iterator for going through all questions
                    # for key, step in enumerate(json_data["steps"]):
                    #     generated_step = llama.get_steps(self.med, self.guide, key)
                    #     if step["key"] == generated_step["key"]:
                    #         step.update(generated_step)

                self.progress += 1
                return json_data
        except Exception as err:
            print(f"Error in reading json file: {err}")
            return None



