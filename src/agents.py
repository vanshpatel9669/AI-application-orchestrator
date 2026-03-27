from src.prompts import (
    JD_EXTRACTION_PROMPT,
    RESUME_EXTRACTION_PROMPT,
    GAP_ANALYSIS_PROMPT,
    BULLET_REWRITE_PROMPT,
    SUMMARY_PROMPT,
    EMAIL_PROMPT,
    INTERVIEW_PROMPT,
    QA_PROMPT,
)
from src.llm_client import generate_text
from src.utils import safe_load_json, clamp_score


def extract_job_requirements(job_description: str) -> dict:
    prompt = JD_EXTRACTION_PROMPT.format(job_description=job_description)
    response = generate_text(prompt)
    data = safe_load_json(response)

    return {
        "title": data.get("title", ""),
        "required_skills": data.get("required_skills", []),
        "preferred_skills": data.get("preferred_skills", []),
        "responsibilities": data.get("responsibilities", []),
        "keywords": data.get("keywords", []),
    }


def extract_candidate_profile(resume_text: str) -> dict:
    prompt = RESUME_EXTRACTION_PROMPT.format(resume_text=resume_text)
    response = generate_text(prompt)
    data = safe_load_json(response)

    return {
        "name": data.get("name", ""),
        "skills": data.get("skills", []),
        "experience": data.get("experience", []),
        "projects": data.get("projects", []),
        "education": data.get("education", []),
    }


def run_gap_analysis(job_requirements: dict, candidate_profile: dict) -> dict:
    prompt = GAP_ANALYSIS_PROMPT.format(
        job_requirements=job_requirements,
        candidate_profile=candidate_profile,
    )
    response = generate_text(prompt)
    data = safe_load_json(response)

    return {
        "matched_skills": data.get("matched_skills", []),
        "missing_skills": data.get("missing_skills", []),
        "strengths": data.get("strengths", []),
        "improvement_areas": data.get("improvement_areas", []),
        "fit_score": clamp_score(data.get("fit_score", 0)),
    }


def rewrite_resume_bullets(job_requirements: dict, candidate_profile: dict, gap_analysis: dict) -> str:
    prompt = BULLET_REWRITE_PROMPT.format(
        job_requirements=job_requirements,
        candidate_profile=candidate_profile,
        gap_analysis=gap_analysis,
    )
    return generate_text(prompt)


def generate_summary(job_requirements: dict, candidate_profile: dict) -> str:
    prompt = SUMMARY_PROMPT.format(
        job_requirements=job_requirements,
        candidate_profile=candidate_profile,
    )
    return generate_text(prompt)


def generate_recruiter_email(job_title: str, company_name: str, candidate_profile: dict) -> str:
    prompt = EMAIL_PROMPT.format(
        job_title=job_title,
        company_name=company_name,
        candidate_profile=candidate_profile,
    )
    return generate_text(prompt)


def generate_interview_questions(job_requirements: dict, candidate_profile: dict) -> str:
    prompt = INTERVIEW_PROMPT.format(
        job_requirements=job_requirements,
        candidate_profile=candidate_profile,
    )
    return generate_text(prompt)


def run_quality_review(job_requirements: dict, candidate_profile: dict, generated_outputs: dict) -> str:
    prompt = QA_PROMPT.format(
        job_requirements=job_requirements,
        candidate_profile=candidate_profile,
        generated_outputs=generated_outputs,
    )
    return generate_text(prompt)