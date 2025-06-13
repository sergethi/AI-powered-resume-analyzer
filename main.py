
from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from resume_parser import extract_text_by_filetype
from keyword_matcher import analyze_keywords
import uuid
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_resume(resume: UploadFile, job_description: str = Form(...)):
    # Extract the file extension (e.g., '.pdf', '.docx') from the uploaded resume's filename
    # os.path.splitext() splits the filename into (name, extension)
    # [-1] gets the extension part, and .lower() ensures consistency in casing
    ext = os.path.splitext(resume.filename)[-1].lower()
    # Generate a unique temporary filename using a UUID and append the original file extension
    # This avoids filename collisions and ensures the file has the correct format
    temp_filename = f"temp_{uuid.uuid4().hex}{ext}"
    file_bytes = await resume.read()

    resume_text = extract_text_by_filetype(temp_filename, file_bytes)
    result = analyze_keywords(resume_text, job_description)
    return result
