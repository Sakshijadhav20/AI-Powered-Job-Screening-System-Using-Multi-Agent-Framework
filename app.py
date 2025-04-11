# app.py

import streamlit as st
from utils import extract_text_from_file, calculate_match_score

st.set_page_config(page_title="AI-Powered Job Screening", layout="centered")

st.title("🤖 AI-Powered Job Application Screening System")
st.markdown("---")

st.markdown("### 📄 Upload Job Description (PDF, DOCX, or TXT)")
jd_file = st.file_uploader("Drop the JD file here", type=["pdf", "docx", "txt"], key="jd")

st.markdown("### 👤 Upload Resume (PDF, DOCX, or TXT)")
resume_file = st.file_uploader("Drop the Resume file here", type=["pdf", "docx", "txt"], key="resume")

if jd_file and resume_file:
    with st.spinner("Reading files..."):
        jd_text = extract_text_from_file(jd_file)
        resume_text = extract_text_from_file(resume_file)
        score = calculate_match_score(resume_text, jd_text)

    st.markdown("---")
    st.markdown("## 📝 Screening Results")
    st.markdown(f"📌 **{resume_file.name}**")
    
    if score > 0:
        st.markdown(f"**Match Score:** `{score}%`")
        if score >= 80:
            st.success("✅ Shortlisted for Interview!")
        else:
            st.warning("⚠️ Not shortlisted. Try improving the resume.")
    else:
        st.error("❌ Failed to compute match score. Please upload valid files.")

    with st.expander("🔍 View Job Description Text"):
        st.write(jd_text or "No text extracted.")
    with st.expander("🔍 View Resume Text"):
        st.write(resume_text or "No text extracted.")
