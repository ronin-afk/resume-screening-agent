import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import re
import pandas as pd

# ----------------------
# Load API Key
# ----------------------
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ----------------------
# Function to get Gemini/Google AI response
# ----------------------
def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)
    return response.text

# ----------------------
# Extract text from uploaded PDF
# ----------------------
def extract_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

# ----------------------
# Streamlit UI
# ----------------------
st.title("📊 Smart ATS Resume Ranking System")
st.text("Upload multiple resumes and rank them based on job description")

jd = st.text_area("Paste the Job Description Here")

uploaded_files = st.file_uploader(
    "Upload Resumes (PDFs)", 
    type="pdf",
    accept_multiple_files=True,
    help="You can upload multiple resumes"
)

submit = st.button("Rank Resumes")

# ----------------------
# When submit is clicked
# ----------------------
if submit:
    if not jd:
        st.error("Please enter the Job Description!")
    elif not uploaded_files:
        st.error("Please upload at least one resume!")
    else:
        results = []

        for uploaded_file in uploaded_files:
            resume_text = extract_pdf_text(uploaded_file)

            # Prompt for ATS evaluation
            prompt = f"""
You are a highly skilled, expert-level ATS (Application Tracking System) with extensive 
knowledge in technology, software engineering, data science, data analytics, and big data roles. 
Your task is to evaluate resumes against a job description with extreme accuracy. 

You must consider that the job market is very competitive. Provide actionable feedback and detailed analysis.

Instructions:
1. Compare the resume against the job description.
2. Calculate a **JD Match Percentage** (0-100%) based on how well the resume aligns with the JD.
3. Identify **Missing Keywords** that are important for the role.
4. Provide a **Profile Summary** highlighting the candidate's skills, experience, and strengths.
5. Be precise and concise, avoid irrelevant information.
6. Use bullet points where appropriate.

Resume: {resume_text}

Job Description: {jd}

Expected Response:
JD Match: <percentage_match>%
Missing Keywords: [keyword1, keyword2, ...]
Profile Summary:
- Summary bullet 1
- Summary bullet 2
- Summary bullet 3
"""

            with st.spinner(f"Evaluating {uploaded_file.name}..."):
                response = get_gemini_response(prompt)

            # Extract percentage match using regex
            match = re.search(r"JD Match:\s*(\d+)%", response)
            score = int(match.group(1)) if match else 0

            results.append({
                "Resume": uploaded_file.name,
                "Score (%)": score,
                "Evaluation": response
            })

        # Sort by score
        results = sorted(results, key=lambda x: x["Score (%)"], reverse=True)

        # Show ranking
        st.subheader("📌 Resume Ranking")
        df = pd.DataFrame(results)[["Resume", "Score (%)"]]
        st.table(df)

        # Optionally show detailed evaluation for each resume
        st.subheader("Detailed Evaluations")
        for r in results:
            st.markdown(f"### 📄 {r['Resume']}")
            st.text(r["Evaluation"])
            st.write("---")
