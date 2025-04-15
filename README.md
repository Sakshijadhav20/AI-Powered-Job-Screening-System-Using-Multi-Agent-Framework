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
├── app.py                     # 🎯 Main Streamlit web app
├── utils.py                   # 🛠️ Helper functions (text parsing, similarity scoring, etc.)
│
├── data/
│   ├── resumes/               # 📄 Uploaded resumes (PDF/DOCX files)
│   └── job_descriptions/      # 📃 Uploaded job descriptions (PDF/TXT files)
│
├── database/
│   └── screening.db           # 🗄️ SQLite database for storing screening results
│
└── README.md                  # 📘 Project documentation (you’re here!)


🧠 How It Works

1. Extracts text from both the JD and resume
2. Uses TF-IDF vectorization to compare similarity
3. Shortlists candidates based on a match threshold
4. Optionally, GPT agents can improve scoring and email drafting


📬 Contact

For any queries, reach out to:
Sakshi Jadhav – sakshijad937@gmail.com
