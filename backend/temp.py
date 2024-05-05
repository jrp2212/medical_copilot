from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from case import Case
from db import DB

import torch
import os
import llama_functions as llama



med = """Patient Name: Mickey Mouse
Date of Birth: 01/01/1970 
Ordering Physician: Minnie Mouse 
Attending Physician: Minnie House MR 
Number: #090901
Age: 53
Sex: M
Report: #89917 Room/Svc: Room F

PROCEDURE: XR Lumbar Spine, 4 views 
DATE: 12/10/2021
COMPARISON: None available
HISTORY: Patient involved in a motor vehicle accident, reporting lumbar pain. Initial encounter.
PATIENT DETAILS: 53M 
ACCOUNT NUMBER: 4567893 ROOM/SERVICE: ED
REPORT NUMBER: 96728622

FINDINGS:
Vertebral Alignment: Normal lumbar curvature with satisfactory alignment of vertebral bodies.
Vertebral Bodies: Demonstrate normal height and bone density. No evidence of compression fractures or pathological lesions.
Disc Spaces: Intervertebral disc spaces are preserved,
Pedicles and Processes: Pedicles, transverse, and spinous processes appear intact with no signs of fractures or deformities.
Facet Joints: Normal facet joint alignment without signs of subluxation or degenerative changes.
Additional Findings: Mild incidental age-related changes such as slight osteophytic lipping noted at L4/L5. No acute bony abnormalities.
Sacral Region: S1 vertebra shows a bifid appearance, which si a congenital variant and is asymptomatic. Sacroiliac joints appear intact.
Others: No visualized abnormalities in the lower thoracic vertebrae.

IMPRESSION: 
Normal lumbar spine X-ray post-motor vehicle accident. No evidence of acute traumatic injury or significant pathology. Incidental findings of mild age-related changes, not uncommon in adults. S1 vertebral bifid appearance noted as a congenital variant: Clinical correlation recommended if symptoms persist.

Clinical Encounter Report

Visit Date: 12/10/2021
Rendering Physician: Minnie Mouse Location: Emergency Department
Patient Information:
Name: Mickey Mouse 
Age: 53
Sex: Male
MR Number: #090901

Chief Complaint: 
Patient presents with lower back pain following a motor vehicle accident.

History of Present Illness (HPI): 
The patient was involved in a motor vehicle accident earlier today. He reports persistent lower back pain since the accident. No loss of consciousness or other injuries reported. 

Review of Systems (ROS):
Constitutional: No fever, chills, weight loss, or fatigue.
Eyes: Denies visual loss, double vision, or eye pain.
ENT: No earache, nasal congestion, sore throat, or hoarseness.
Cardiovascular: Denies chest pain, palpitations, or edema.
Respiratory: No shortness of breath, cough, or wheezing.
Gastrointestinal: No abdominal pain, nausea, vomiting, diarrhea, or constipation. Genitourinary: Denies dysuria, frequency, or hematuria.
Skin: No rashes, itching, or bruising.
Neurological: Positive straight leg raise; denies headaches, dizziness, seizures, or numbness.
Psychiatric: Denies anxiety, depression, or changes in sleep patterns. Endocrine: No history of diabetes or thyroid disease. Hematologic/Lymphatic: No history of bleeding disorders or anemia. Allergic/Immunologic: No known allergies or autoimmune disorders.

Physical Examination:
General: Alert, oriented, and ni no acute distress.
Vital Signs: Blood pressure 120/80 m m H , Heart rate 78 bpm, Respiratory rate 16/min, Temperature 98.6°F.
HEENT: Head is normocephalic/atraumatic. Pupils are equal, round, reactive to light. No nasal discharge. Oropharynx is clear.
Cardiovascular: Regular rate and rhythm, no murmurs, rubs, or gallops.
Respiratory: Lungs clear toauscultation bilaterally, nowheezes, crackles, or rhonchi. Abdomen: Soft, non-tender, non-distended, no guarding or rebound, Bowel sounds are normal.
Musculoskeletal: Tenderness to palpation in the lower lumbar paraspinal muscles. •Full range of motion with discomfort. No deformities.
Neurological: Cranial nerves II-XII intact. Motor strength 5/5 in all extremities. 'Sensation intact.
Skin: No rashes, lesions, or bruising.

Diagnostic Tests:
Lumbar spine X-ray: No acute abnormalities, mild age-related changes. Laboratory Results:
Complete Blood Count (CBC):
White Blood Cell (WBC) count: 6.0 × 103⁄4L (normal range: 4.5-11.0 x 103⁄4L)
Red Blood Cell (RBC) count: 4.8 x 10%L (normal range: 4.7-6.1 x
10%L for males)
Hemoglobin (Hgb): 14.2 g/dL (normal range: 13.8-17.2 g/dL for males)
Hematocrit (Hct): 42% (normal range: 40.7-50.3% for males)
Mean Corpuscular Volume (MCV): 87 Lf (normal range: 80-96 fL)
Mean Corpuscular Hemoglobin (MCH): 29 pg (normal range: 27-33 pg)
Mean Corpuscular Hemoglobin Concentration (MCHC): 3 g/dL
(normal range: 31-37 g/dL) 
Platelet count: 250x 103⁄4/L (normal range: 150-450 x 103⁄4uL)
Neutrophils: 60% (normal range: 40-70%)
Lymphocytes: 30% (normal range: 20-40%)
Monocytes: 7% (normal range: 2-8%)
Eosinophils: 3% (normal range: 1-4%)
Basophils: 0% (normal range: 0-2%).
Comprehensive Metabolic Panel (CMP): Normal. Erythrocyte Sedimentation Rate (ESR): Normal.
C-Reactive Protein (CRP): Normal.
Prothrombin Time (PT): 11.0 seconds (normal range: 9.5-13.5 seconds). International Normalized Ratio (INR): 1.0 (normal range: 0.8-1.2).
Partial Thromboplastin Time (PTT): 30 seconds (normal range: 25-35 seconds).

Assessment/Plan:
Diagnosis: Suspected lumbar strain with possible nerve root irritation secondary to motor vehicle accident.
Management: Prescribed NSAIDs and muscle relaxants. Advised rest, heat/cold therapy, and physical therapy referral.
Follow-up: Recommended follow-up with primary care or spine specialist if symptoms persist or worsen.
Disposition:
Discharged home with pain management andfollow-up instructions 
Provider: Minnie Mouse, MD
"""
guide = ""





def load_or_download_model(model_name: str, model_dir: str):
    if not os.path.exists(model_dir):
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
model_dir = "models/llama3"  # Specify the directory to save/load the model
model = load_or_download_model(model_name, model_dir)
tokenizer = AutoTokenizer.from_pretrained(model_name)

print(llama.get_summary(model, tokenizer, med, guide))