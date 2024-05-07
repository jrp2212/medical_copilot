from fastapi import FastAPI, Query, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from case import Case
from db import DB
import llama_functions as llama

db = DB()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# spin up llama3 at startup and unload cache when shutting down
@app.on_event("startup")
async def startup_event():
    model_name = "meta-llama/Meta-Llama-3-8B-Instruct"
    model_dir = "models/llama3"
    llama.load_model(model_name, model_dir)

@app.on_event("shutdown")
async def shutdown_event():
    llama.unload_model()


# ---------------------------------------------------------------------------
# POST /cases
# creates a new case with a unique id, adds it to our DB
@app.post("/cases")
async def create_case(request: Request):
    try:
        payload = await request.json()
        case = Case(payload)
        db.put(case.case_id, case)
        print(f"created case_id: {case.case_id}. Count: {db.length()}")
        return {"id": case.case_id}
    except Exception as err:
        msg = f"error in creating case: {str(err)}"
        print(msg)
        raise HTTPException(status_code=500, detail=msg)

# ---------------------------------------------------------------------------
# GET /cases/<case_id>
# get a single case based on case_id
@app.get("/cases/{case_id}")
async def get_case(case_id: str):
    try:
        case = db.get(case_id)
        return case.to_json()
    except:
        raise HTTPException(status_code=404, detail="case not found")
    
# ---------------------------------------------------------------------------
# GET /cases
# get all the available cases in the DB using standard pagination
@app.get("/cases")
async def get_all_cases(page: int = Query(1, alias="page"), size: int = Query(20, alias="size")):
    try:
        getter = lambda case: case.to_json()
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


