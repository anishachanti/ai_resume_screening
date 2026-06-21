import re

SKILLS_DB = [
    "Java",
    "Python",
    "Spring Boot",
    "React",
    "Docker",
    "AWS",
    "Oracle",
    "SQL",
    "MongoDB",
    "Microservices",
    "Kubernetes",
    "Git",
    "HTML",
    "CSS",
    "JavaScript"
]

def extract_email(text):

    email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
    match = re.search(
        email_pattern,
        text
    )


    return match.group(0) if match else None



def extract_phone(text):
    match = re.search(
        r"\+?\d[\d\s\-]{8,15}",
        text
    )

    return match.group(0).strip() if match else None

def extract_skills(text):

    found_skills = []

    for skill in SKILLS_DB:

        if skill.lower() in text.lower():
            found_skills.append(skill)

    return list(set(found_skills))

def extract_name(text):

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line) > 3 and len(line.split()) <= 4:
            return line

    return "Unknown"

