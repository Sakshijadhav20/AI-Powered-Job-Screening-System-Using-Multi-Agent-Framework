# utils.py

import PyPDF2
import docx2txt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_file(file):
    if file is None:
        return ""
    
    file_name = file.name.lower()

    if file_name.endswith('.pdf'):
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() or ''
        return text.strip()

    elif file_name.endswith('.docx'):
        return docx2txt.process(file)

    elif file_name.endswith('.txt'):
        return file.read().decode('utf-8').strip()

    return ""

def calculate_match_score(resume_text, jd_text):
    documents = [resume_text, jd_text]
    
    if not resume_text.strip() or not jd_text.strip():
        return 0.0
    
    tfidf = TfidfVectorizer(stop_words='english')
    try:
        tfidf_matrix = tfidf.fit_transform(documents)
        score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        return round(score * 100, 2)
    except ValueError:
        return 0.0
