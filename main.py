# main.py

import os
import pandas as pd
from PyPDF2 import PdfReader
from job_description_summarizer import JobDescriptionSummarizer
from recruiting_agent import RecruitingAgent
from interview_scheduler import generate_interview_email
from database_manager import DatabaseManager

def extract_text_from_file(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def main():
    # Load Job Descriptions from Excel
    jd_df = pd.read_excel("data/job_description.csv")

    # For each JD in Excel
    for index, row in jd_df.iterrows():
        job_title = row["Job Title"]
        jd_text = row["Job Description"]
        jd_summary = JobDescriptionSummarizer(jd_text).summarize()

        print(f"\n🔍 Processing Job: {job_title}")

        # Loop through all PDFs in the cvs folder
        cv_folder = "data/cvs"
        for cv_file in os.listdir(cv_folder):
            if cv_file.endswith(".pdf"):
                cv_path = os.path.join(cv_folder, cv_file)
                cv_text = extract_text_from_file(cv_path)

                agent = RecruitingAgent(cv_text)
                match_score = agent.calculate_match_score(jd_summary)

                print(f"📄 {cv_file} -> Score: {match_score}%")

                if match_score >= 80:
                    candidate_name = cv_file.replace("_resume.pdf", "").title()
                    email = generate_interview_email(candidate_name, job_title, match_score)
                    print(f"\n📬 Email to {candidate_name}:\n{email}\n")

                    db = DatabaseManager()
                    db.insert_candidate(candidate_name, match_score)
                    db.close()

if __name__ == "__main__":
    main()
