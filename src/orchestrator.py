from concurrent.futures import ThreadPoolExecutor
from src.agents import (
    extract_job_requirements,
    extract_candidate_profile,
    run_gap_analysis,
    rewrite_resume_bullets,
    generate_summary,
    generate_recruiter_email,
    generate_interview_questions,
    run_quality_review,
)


def run_pipeline(resume_text: str, job_description: str, company_name: str = "Target Company") -> dict:
    job_requirements = extract_job_requirements(job_description)
    candidate_profile = extract_candidate_profile(resume_text)
    gap_analysis = run_gap_analysis(job_requirements, candidate_profile)

    with ThreadPoolExecutor(max_workers=4) as executor:
        bullets_future = executor.submit(
            rewrite_resume_bullets,
            job_requirements,
            candidate_profile,
            gap_analysis,
        )

        summary_future = executor.submit(
            generate_summary,
            job_requirements,
            candidate_profile,
        )

        email_future = executor.submit(
            generate_recruiter_email,
            job_requirements.get("title", "Target Role"),
            company_name,
            candidate_profile,
        )

        interview_future = executor.submit(
            generate_interview_questions,
            job_requirements,
            candidate_profile,
        )

        rewritten_bullets = bullets_future.result()
        tailored_summary = summary_future.result()
        recruiter_email = email_future.result()
        interview_questions = interview_future.result()

    generated_outputs = {
        "rewritten_bullets": rewritten_bullets,
        "tailored_summary": tailored_summary,
        "recruiter_email": recruiter_email,
        "interview_questions": interview_questions,
    }

    quality_review = run_quality_review(
        job_requirements,
        candidate_profile,
        generated_outputs,
    )

    return {
        "job_requirements": job_requirements,
        "candidate_profile": candidate_profile,
        "gap_analysis": gap_analysis,
        "rewritten_bullets": rewritten_bullets,
        "tailored_summary": tailored_summary,
        "recruiter_email": recruiter_email,
        "interview_questions": interview_questions,
        "quality_review": quality_review,
    }