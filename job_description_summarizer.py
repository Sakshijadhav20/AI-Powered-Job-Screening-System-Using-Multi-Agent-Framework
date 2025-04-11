# job_description_summarizer.py

import re

class JobDescriptionSummarizer:
    def __init__(self, jd_text):
        self.jd_text = jd_text.lower()

    def extract_skills(self):
        skill_keywords = ['python', 'java', 'sql', 'machine learning', 'deep learning',
                          'communication', 'project management', 'data analysis']
        return [skill for skill in skill_keywords if skill in self.jd_text]

    def extract_experience(self):
        match = re.search(r'(\d+)\+?\s*years? of experience', self.jd_text)
        return int(match.group(1)) if match else 0

    def extract_qualifications(self):
        qualifications = []
        if 'bachelor' in self.jd_text or 'b.e' in self.jd_text:
            qualifications.append('Bachelor')
        if 'master' in self.jd_text or 'm.e' in self.jd_text:
            qualifications.append('Master')
        if 'phd' in self.jd_text:
            qualifications.append('PhD')
        return qualifications

    def extract_responsibilities(self):
        lines = self.jd_text.split('\n')
        responsibilities = [line.strip('-• ') for line in lines if 'responsible' in line or 'develop' in line or 'manage' in line]
        return responsibilities

    def summarize(self):
        return {
            'skills': self.extract_skills(),
            'experience': self.extract_experience(),
            'qualifications': self.extract_qualifications(),
            'responsibilities': self.extract_responsibilities()
        }

# Example usage
if __name__ == "__main__":
    jd = """
    We are looking for a Python developer with 2+ years of experience.
    Required Skills: Python, SQL, Machine Learning, Communication.
    Responsibilities include developing ML models and managing data pipelines.
    Education: Bachelor's degree in Computer Science.
    """
    summarizer = JobDescriptionSummarizer(jd)
    summary = summarizer.summarize()
    print(summary)
