# recruiting_agent.py

import re

class RecruitingAgent:
    def __init__(self, cv_text):
        self.cv_text = cv_text.lower()

    def extract_skills(self):
        skill_keywords = ['python', 'java', 'sql', 'machine learning', 'deep learning',
                          'communication', 'project management', 'data analysis']
        return [skill for skill in skill_keywords if skill in self.cv_text]

    def extract_experience(self):
        match = re.search(r'(\d+)\+?\s*years? of experience', self.cv_text)
        return int(match.group(1)) if match else 0

    def extract_qualifications(self):
        qualifications = []
        if 'bachelor' in self.cv_text or 'b.e' in self.cv_text:
            qualifications.append('Bachelor')
        if 'master' in self.cv_text or 'm.e' in self.cv_text:
            qualifications.append('Master')
        if 'phd' in self.cv_text:
            qualifications.append('PhD')
        return qualifications

    def extract_candidate_info(self):
        return {
            'skills': self.extract_skills(),
            'experience': self.extract_experience(),
            'qualifications': self.extract_qualifications()
        }

    def calculate_match_score(self, jd_summary):
        candidate_info = self.extract_candidate_info()

        skill_match = len(set(candidate_info['skills']) & set(jd_summary['skills']))
        total_required_skills = len(jd_summary['skills']) or 1

        skill_score = (skill_match / total_required_skills) * 100

        experience_match = min(candidate_info['experience'], jd_summary['experience'])
        experience_score = 100 if experience_match >= jd_summary['experience'] else (experience_match / jd_summary['experience']) * 100

        qualification_match = any(q in candidate_info['qualifications'] for q in jd_summary['qualifications'])
        qualification_score = 100 if qualification_match else 0

        final_score = round((0.5 * skill_score + 0.3 * experience_score + 0.2 * qualification_score), 2)

        return final_score

# Example usage
if __name__ == "__main__":
    from job_description_summarizer import JobDescriptionSummarizer

    jd_text = """
    We are looking for a Python developer with 2+ years of experience.
    Required Skills: Python, SQL, Machine Learning, Communication.
    Education: Bachelor's degree in Computer Science.
    """
    cv_text = """
    I have 3 years of experience in Python and Machine Learning.
    Skills: Python, SQL, Communication.
    Education: Bachelor of Engineering in IT.
    """

    jd_summary = JobDescriptionSummarizer(jd_text).summarize()
    agent = RecruitingAgent(cv_text)
    score = agent.calculate_match_score(jd_summary)
    print(f"Match Score: {score}%")
