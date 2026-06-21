# AI Resume Screening Platform with MCP

## Overview

AI Resume Screening Platform is an intelligent recruitment assistant that helps recruiters evaluate, rank, and compare candidates against job descriptions using Large Language Models (Groq LLM).

The platform consists of:

* React Frontend Dashboard
* FastAPI Backend
* Groq LLM Integration
* PDF Resume Parsing
* MCP (Model Context Protocol) Server for AI Agent Integration

---

## Features

### Resume Parsing

* Extract candidate information from PDF resumes
* Name extraction
* Email extraction
* Phone number extraction
* Skills extraction

### AI Candidate Evaluation

* Resume vs Job Description matching
* Candidate scoring (0-100)
* Hiring recommendation generation
* Strength analysis
* Missing skill analysis
* Candidate summary generation

### Candidate Ranking

* Upload a Job Description
* Upload multiple resumes
* Automatically rank candidates by suitability
* Sort candidates based on AI-generated scores

### Candidate Comparison

* Compare two candidates side-by-side
* Compare scores
* Compare strengths
* Compare missing skills
* Identify the stronger candidate

### MCP Integration

Expose recruitment capabilities as MCP tools:

* evaluate_candidate
* rank_candidates
* compare_candidates
* evaluate_pdf_candidate

These tools can be used directly from Claude Desktop and other MCP-compatible AI clients.

---

## Architecture

```text
React Frontend
      |
      v
FastAPI Backend
      |
      v
PDF Parsing (PyMuPDF)
      |
      v
Groq LLM
      |
      v
Candidate Evaluation

Claude Desktop
      |
      v
MCP Server
      |
      v
Resume Screening Tools
```

---

## Tech Stack

### Frontend

* React
* Axios
* Bootstrap
* React Bootstrap

### Backend

* FastAPI
* Python
* PyMuPDF
* Groq API
* Python Dotenv

### MCP

* FastMCP
* Claude Desktop

---

## Project Structure

```text
ai-resume-screening/

├── backend/
│   ├── app.py
│   ├── ai_service.py
│   ├── pdf_utils.py
│   ├── resume_parser.py
│   ├── matching_service.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── package.json
│
├── mcp-server/
│   ├── server.py
│   └── requirements.txt
│
├── .gitignore
└── README.md
```

---

## Setup

### Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app:app --reload
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

### MCP Server

```bash
cd mcp-server

pip install -r requirements.txt

python server.py
```

---

## Environment Variables

Create:

```text
backend/.env
```

```env
GROQ_API_KEY=your_groq_api_key_here
```




