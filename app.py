import streamlit as st
from src.pdf_parser import extract_text_from_pdf
from src.orchestrator import run_pipeline
from src.exporter import build_report_text

st.set_page_config(page_title="MoJoHire", page_icon="🚀", layout="wide")

st.title("MoJoHire")
st.caption("AI Job Application Orchestrator")

st.write(
    "Upload a resume and paste a job description to generate a tailored application package."
)

with st.sidebar:
    st.header("Input")
    company_name = st.text_input("Company Name", placeholder="e.g. OpenAI")
    uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

job_description = st.text_area(
    "Paste Job Description",
    height=300,
    placeholder="Paste the full job description here..."
)

generate_clicked = st.button("Generate Application Package", use_container_width=True)

if generate_clicked:
    if uploaded_resume is None:
        st.error("Please upload a resume PDF.")
    elif not job_description.strip():
        st.error("Please paste a job description.")
    else:
        with st.spinner("Running orchestration pipeline..."):
            resume_text = extract_text_from_pdf(uploaded_resume)
            results = run_pipeline(
                resume_text=resume_text,
                job_description=job_description,
                company_name=company_name or "Target Company",
            )

        st.success("Application package generated successfully.")
        st.markdown("## Orchestration Flow")
        st.info(
    "Pipeline: Resume ingestion → Structured job requirement extraction → Candidate profiling → "
    "Skill gap analysis → Parallel downstream generation (summary, bullets, outreach, interview prep) → "
    "Final QA validation layer"
)

        fit_score = results["gap_analysis"]["fit_score"]

        st.subheader("Fit Score")
        st.progress(fit_score / 100)
        st.metric("Estimated Match", f"{fit_score}%")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("## Job Requirements")
            st.markdown(f"**Target Role:** {results['job_requirements'].get('title', 'N/A')}")

            st.markdown("**Required Skills**")
            for skill in results["job_requirements"].get("required_skills", []):
                st.write(f"- {skill}")

            st.markdown("**Preferred Skills**")
            for skill in results["job_requirements"].get("preferred_skills", []):
                st.write(f"- {skill}")

            st.markdown("**Responsibilities**")
            for item in results["job_requirements"].get("responsibilities", []):
                st.write(f"- {item}")

            with st.expander("View Raw Job Requirement JSON"):
                st.json(results["job_requirements"])

            st.markdown("## Candidate Profile")
            st.markdown(f"**Name:** {results['candidate_profile'].get('name', 'N/A')}")

            st.markdown("**Top Skills**")
            for skill in results["candidate_profile"].get("skills", [])[:12]:
                st.write(f"- {skill}")

            with st.expander("View Raw Candidate Profile JSON"):
             st.json(results["candidate_profile"])

            st.markdown("## Gap Analysis")

            st.markdown("**Matched Skills**")
            for skill in results["gap_analysis"].get("matched_skills", []):
             st.write(f"- {skill}")

            st.markdown("**Missing Skills**")
            for skill in results["gap_analysis"].get("missing_skills", []):
                st.write(f"- {skill}")

            st.markdown("**Strengths**")
            for item in results["gap_analysis"].get("strengths", []):
                st.write(f"- {item}")

            st.markdown("**Improvement Areas**")
            for item in results["gap_analysis"].get("improvement_areas", []):
                st.write(f"- {item}")

            with st.expander("View Raw Gap Analysis JSON"):
                st.json(results["gap_analysis"])

        with col2:
            st.markdown("## Tailored Professional Summary")
            st.write(results["tailored_summary"])

            st.markdown("## Rewritten Resume Bullets")
            st.write(results["rewritten_bullets"])

            st.markdown("## Recruiter Outreach Email")
            st.write(results["recruiter_email"])

            st.markdown("## Interview Questions")
            st.write(results["interview_questions"])

            st.markdown("## QA Review")
            st.write(results["quality_review"])

        report_text = build_report_text(results)

        st.download_button(
            label="Download Report",
            data=report_text,
            file_name="mojohire_report.txt",
            mime="text/plain",
        )