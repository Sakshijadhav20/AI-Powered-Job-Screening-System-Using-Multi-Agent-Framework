# 🧠 AI-Powered Job Screening System

This project is a smart recruitment assistant that automates the screening of resumes based on uploaded job descriptions using AI and text intelligence.

## 🔍 Problem Statement

Manual resume screening is tedious and error-prone. Recruiters spend hours filtering resumes for each job opening. This system solves that by automating JD-resume matching with AI.

## ✅ Features

- 📄 Upload job descriptions (PDF/TXT)
- 📎 Upload candidate resumes (PDF/DOCX)
- 🤖 Automatically extract key information
- 📊 Generate a match score based on skill, experience, and keyword match
- 📧 Auto-generate interview invite emails
- 🧩 Modular design using multiple AI agents
- 🧠 Optional GPT/LangChain integration
- 📦 SQLite for persistent storage

## 🧰 Tech Stack

- Python
- Streamlit (for UI)
- PyPDF2 & python-docx (for file parsing)
- Scikit-learn (TF-IDF for similarity scoring)
- LangChain / GPT (optional)
- SQLite (for storing data)

## 📁 Folder Structure

AI-Powered-Job-Screening/
│
├── app.py                 # Main Streamlit app
├── utils.py               # Helper functions (text extraction, scoring, etc.)
├── data/
│   ├── resumes/           # Uploaded resumes (PDF/DOCX)
│   └── job_descriptions/  # Uploaded JDs (PDF/TXT)
├── database/
│   └── screening.db       # SQLite DB for saved results
└── README.md              # You're here!



🧠 How It Works

1. Extracts text from both the JD and resume
2. Uses TF-IDF vectorization to compare similarity
3. Shortlists candidates based on a match threshold
4. Optionally, GPT agents can improve scoring and email drafting


📌 Future Enhancements

1. Resume and JD parsing using LangChain Agents
2. Cloud-based storage and database
3. Support for bulk screening
4. Enhanced UI/UX with animations

🙌 Acknowledgements

This project draws inspiration from open-source projects and aims to assist HR professionals and recruiters with intelligent resume screening.


📬 Contact

For any queries, reach out to:
Sakshi Jadhav – sakshijad937@gmail.com
