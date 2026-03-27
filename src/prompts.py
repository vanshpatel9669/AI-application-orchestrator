JD_EXTRACTION_PROMPT = """
You are an expert job description parser.

Your task:
Extract the following from the job description and return STRICT JSON only.

Schema:
{{
  "title": "string",
  "required_skills": ["string"],
  "preferred_skills": ["string"],
  "responsibilities": ["string"],
  "keywords": ["string"]
}}

Rules:
- Do not include markdown.
- Do not include explanations.
- Keep items concise and deduplicated.
- Extract ATS-style keywords where possible.

Job Description:
{job_description}
"""


RESUME_EXTRACTION_PROMPT = """
You are an expert resume parser.

Your task:
Extract the following from the resume and return STRICT JSON only.

Schema:
{{
  "name": "string",
  "skills": ["string"],
  "experience": ["string"],
  "projects": ["string"],
  "education": ["string"]
}}

Rules:
- Do not include markdown.
- Do not include explanations.
- Keep information grounded in the resume.
- Deduplicate repeated skills.

Resume:
{resume_text}
"""


GAP_ANALYSIS_PROMPT = """
You are evaluating candidate-job fit.

Compare the job requirements and candidate profile.
Return STRICT JSON only.

Schema:
{{
  "matched_skills": ["string"],
  "missing_skills": ["string"],
  "strengths": ["string"],
  "improvement_areas": ["string"],
  "fit_score": 0
}}

Rules:
- fit_score must be an integer from 0 to 100.
- Do not exaggerate.
- Base everything on the provided data only.

Job Requirements:
{job_requirements}

Candidate Profile:
{candidate_profile}
"""


BULLET_REWRITE_PROMPT = """
You are a senior resume strategist.

Write exactly 4 tailored resume bullets for this target role.

Requirements:
- concise
- ATS-friendly
- realistic
- action-oriented
- metrics-oriented where appropriate
- do not invent tools, frameworks, or achievements not supported by the candidate profile
- if a framework is not explicitly present, use broader wording instead
- align with the job requirements
- each bullet should be one line only

Job Requirements:
{job_requirements}

Candidate Profile:
{candidate_profile}

Gap Analysis:
{gap_analysis}
"""


SUMMARY_PROMPT = """
Write a tailored professional summary for this candidate and role.

Requirements:
- 4 to 5 lines
- modern, strong, ATS-friendly
- specific to the role
- realistic and grounded in the candidate profile
- do not mention specific frameworks unless explicitly supported by the profile
- prefer broader wording like 'agentic workflows', 'LLM applications', or 'RAG pipelines' when needed

Job Requirements:
{job_requirements}

Candidate Profile:
{candidate_profile}
"""


EMAIL_PROMPT = """
Write a concise outreach email that the candidate would send to a recruiter or hiring team.

Requirements:
- written FROM the candidate, not TO the candidate
- professional, polished, confident
- 120 to 170 words
- specific to the role
- no generic filler
- do not invent experience
- end with a short, professional sign-off

Job Title: {job_title}
Company: {company_name}
Candidate Profile: {candidate_profile}
"""


INTERVIEW_PROMPT = """
Generate 10 likely interview questions for this candidate and target role.

Format:
1. Technical
2. Behavioral
3. Project-based

Requirements:
- role-relevant
- realistic
- grounded in the candidate profile
- do not assume direct experience with tools or frameworks unless explicitly listed
- where experience is adjacent, ask broader questions

Job Requirements:
{job_requirements}

Candidate Profile:
{candidate_profile}
"""


QA_PROMPT = """
You are a QA reviewer for AI-generated career materials.

Review the generated outputs.

Check for:
1. consistency with the target role
2. realism
3. non-exaggeration
4. relevance
5. clarity

Write a concise quality review with:
- Overall assessment
- Risks or overclaims
- Suggested improvements

Job Requirements:
{job_requirements}

Candidate Profile:
{candidate_profile}

Generated Outputs:
{generated_outputs}
"""