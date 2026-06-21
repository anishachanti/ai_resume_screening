import os
import json
import re

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key = os.getenv("GROQ_API_KEY")
)

def analyze_resume_with_ai(resume_text):

    prompt = f"""

You are an expert HR recruiter.

Analyze the following resume.

Return ONLY valid JSON.

Resume:
{resume_text}

JSON Format:
{{
  "name": "",
  "email": "",
  "phone": "",
  "skills": [],
  "experience_summary": "",
  "candidate_summary": ""

}}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    content = response.choices[0].message.content

    content = re.sub(r"```json|```","",content).strip()

    try:
        return json.loads(content)
    except Exception as e:
        return {
            "error": str(e),
            "raw_response": content
        }




def evaluate_candidate(resume_text,jd_text):
    prompt = f"""
You are an expert HR recruiter.

Evaluate this candidate against the job description.

IMPORTANT:
- Score MUST be an integer between 0 and 100.
- 90-100 = Excellent Match
- 75-89 = Good Match
- 60-74 = Average Match
- Below 60 = Weak Match


JOB DESCRIPTION:
{jd_text}

RESUME:
{resume_text}

Generate 5 technical interview questions
based on the candidate's skills and the job description.

Return ONLY valid JSON:

{{
   "candidate_name": "",
   "score": 0,
   "recommendation": "",
   "strengths": [],
   "missing_skills": [],
   "interview_questions": [],
   "summary": ""
}}
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    content = response.choices[0].message.content

    content = re.sub(r"```json|```", "", content).strip()

    try:
        return json.loads(content)
    except Exception as e:
        return {
            "error": str(e),
            "raw_response": content
        }