from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from case import Case
from db import DB

import torch
import os



def load_or_download_model(model_name: str, model_dir: str):
    if not os.path.exists(model_dir):
        print("Directory Found")
        os.makedirs(model_dir, exist_ok=True)
    
    try:
        model = AutoModel.from_pretrained(model_dir)
        print("Model loaded from local directory.")
    except Exception as e:
        print("Model not found locally, downloading from Hugging Face.")
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            load_in_8bit=True,
            device_map="auto",
        )

        model.save_pretrained(model_dir)
        print("Model downloaded and saved locally.")
    
    return model

# load llama3
model_name = "meta-llama/Meta-Llama-3-8B-Instruct"  # Specify the model name
model_dir = "/models/llama3"  # Specify the directory to save/load the model
model = load_or_download_model(model_name, model_dir)
tokenizer = AutoTokenizer.from_pretrained(model_name)


# warning: It will wipe out when the server restarts ⚠️
db = DB()

# spin up a Fast API server here
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------
# POST /cases
# creates a new case with a unique id, adds it to our DB
@app.post("/cases")
async def create_case():
    try:
        case = Case(model, tokenizer)
        db.put(case.case_id, case)
        print(f"created case_id: {case.case_id}. Count: {db.length()}")
        return {"id": case.case_id}
    except Exception as err:
        msg = f"error in creating case: {str(err)}"
        raise HTTPException(status_code=500, detail=msg)

# ---------------------------------------------------------------------------
# GET /cases/<case_id>
# get a single case based on case_id
# the .to_json() function is used to handle time-based updates
@app.get("/cases/{case_id}")
async def get_case(case_id: str):
    try:
        # read a case
        case = db.get(case_id)

        # use the to_json() method to get its time-based value
        return case.to_json()
    except:
        raise HTTPException(status_code=404, detail="case not found")
    
# ---------------------------------------------------------------------------
# GET /cases
# get all the available cases in the DB using standard pagination
# e.g. /cases?page=1&size=20
@app.get("/cases")
async def get_all_cases(page: int = Query(1, alias="page"), size: int = Query(20, alias="size")):
    try:
        # this lambda will get the time-based status of each case
        getter = lambda case: case.to_json()

        # read the specified page from the DB, then run map it using
        # the lambda function above. This will give you the final json 
        # for all the cases in the current page
        list_of_cases = list(map(getter, db.paginate(page, size)))
        
        return {
            "total_items": db.length(),
            "current_page": page,
            "items": list_of_cases
        }
    except Exception as err:
        msg = f"error in fetching cases: {str(err)}"
        raise HTTPException(status_code=500, detail=msg)

# ---------------------------------------------------------------------------
# GET /
# return a list of app the available routes on this server
@app.get("/")
async def root():
    url_list = [{"path": route.path, "name": route.name} for route in app.routes]
    return url_list

