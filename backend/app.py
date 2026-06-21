from fastapi import FastAPI, UploadFile, File
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
import uuid


from matching_service import calculate_match
from resume_parser import extract_name,extract_email,extract_phone,extract_skills
from ai_service import analyze_resume_with_ai, evaluate_candidate
import os

from pdf_utils import extract_text_from_pdf

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



UPLOAD_FOLDER = "uploads/resumes"


@app.get("/")
def home():
    return {"message" : "Resume Screening API Running"}


@app.post("/analyze-resume-ai")
async def analyze_resume_ai(file: UploadFile = File(...)):
    file_path = os.path.join("uploads/resumes", file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    resume_text = extract_text_from_pdf(file_path)

    result = analyze_resume_with_ai(resume_text)

    return result


@app.post("/evaluate-candidate")
async def evaluate_candidate_api(resume: UploadFile = File(...), jd: UploadFile = File(...)):
    resume_path = os.path.join("uploads/resumes", f"{uuid.uuid4()}_{resume.filename}")

    with open(resume_path, "wb") as buffer:
        buffer.write(await resume.read())

    jd_path = os.path.join("uploads/jds", jd.filename)

    with open(jd_path, "wb") as buffer:
        buffer.write(await jd.read())

    resume_text = extract_text_from_pdf(resume_path)

    jd_text = extract_text_from_pdf(jd_path)

    result = evaluate_candidate(resume_text, jd_text)

    return result

@app.post("/rank-candidates")
async def rank_candidates(jd: Annotated[UploadFile,File(...)], resumes: Annotated[list[UploadFile], File(...)]):

    jd_path = os.path.join("uploads/jds", jd.filename)
    with open(jd_path, "wb") as buffer:
        buffer.write(await jd.read())

    jd_text = extract_text_from_pdf(jd_path)

    results = []

    for resume in resumes:

        resume_path = os.path.join("uploads/resumes",resume.filename)

        with open(resume_path, "wb") as buffer:
            buffer.write(await resume.read())

        resume_text = extract_text_from_pdf(resume_path)

        evaluation = evaluate_candidate(resume_text, jd_text)

        evaluation["filename"] = resume.filename

        results.append(evaluation)

    results.sort(key=lambda x: x["score"], reverse=True)

    return results



