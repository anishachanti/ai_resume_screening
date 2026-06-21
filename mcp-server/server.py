import sys
import os

backend_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "backend"
    )
)

sys.path.insert(0, backend_path)

from mcp.server.fastmcp import FastMCP

from backend.ai_service import evaluate_candidate
from backend.pdf_utils import extract_text_from_pdf

mcp = FastMCP("Resume Screening MCP")


@mcp.tool()
def evaluate_candidate(resume_text: str,jd_text: str):
    """ Evaluate a candidate against a job description."""
    return evaluate_candidate(resume_text, jd_text)

@mcp.tool()
def rank_candidates(candidates: list[str], jd_text: str):
    """ Rank multiple candidates."""
    results = []

    for candidate in candidates:
        result = evaluate_candidate(candidate, jd_text)
        results.append(result)

    results.sort(key=lambda x: x["score"], reverse=True)

    return results

@mcp.tool()
def compare_candidates(candidate1: dict[str, object],candidate2: dict[str, object]):
    """ Compare two candidates."""
    winner = (candidate1 if candidate1["score"] > candidate2["score"] else candidate2)

    return {"winner": winner["candidate_name"], "score": winner["score"]}

@mcp.tool()
def evaluate_pdf_candidate(resume_path: str, jd_path: str):
    """
     Evaluate a PDF resume against a PDF job description.
    """
    try:
        resume_text = extract_text_from_pdf(resume_path)
        jd_text = extract_text_from_pdf(jd_path)

        return evaluate_candidate(resume_text, jd_text)

    except Exception as e:
        return {
            "error": str(e),
        }

if __name__ == "__main__":
    mcp.run()