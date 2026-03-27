def build_report_text(results: dict) -> str:
    lines = []

    lines.append("MoJoHire Report")
    lines.append("=" * 50)
    lines.append("")

    lines.append("Job Requirements")
    lines.append("-" * 50)
    lines.append(str(results["job_requirements"]))
    lines.append("")

    lines.append("Candidate Profile")
    lines.append("-" * 50)
    lines.append(str(results["candidate_profile"]))
    lines.append("")

    lines.append("Gap Analysis")
    lines.append("-" * 50)
    lines.append(str(results["gap_analysis"]))
    lines.append("")

    lines.append("Tailored Summary")
    lines.append("-" * 50)
    lines.append(results["tailored_summary"])
    lines.append("")

    lines.append("Rewritten Resume Bullets")
    lines.append("-" * 50)
    lines.append(results["rewritten_bullets"])
    lines.append("")

    lines.append("Recruiter Email")
    lines.append("-" * 50)
    lines.append(results["recruiter_email"])
    lines.append("")

    lines.append("Interview Questions")
    lines.append("-" * 50)
    lines.append(results["interview_questions"])
    lines.append("")

    lines.append("Quality Review")
    lines.append("-" * 50)
    lines.append(results["quality_review"])
    lines.append("")

    return "\n".join(lines)