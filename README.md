# 📄 Resume Analyzer

A full-stack AI-powered web application to analyze resumes against job descriptions. The tool highlights matched and missing keywords, providing an overall match score using Natural Language Processing (NLP) techniques.

## 🚀 Features

- Upload resumes in PDF, DOCX, or DOC formats
- Paste a job description
- Get an instant analysis:
  - Match score
  - Matched keywords
  - Missing keywords (filtered by stopwords and stemmed terms)
- Color-coded feedback (green/yellow/red)
- NLP preprocessing with stemming and stopword removal
- Frontend + Backend separation for easy scalability

---

## 🛠️ Tech Stack

### Frontend

- **React** – Core library for building UI
- **Tailwind CSS** – For responsive, utility-first styling
- **Axios** – For communicating with the FastAPI backend

### Backend

- **FastAPI** – Lightweight and fast Python framework for API endpoints
- **pdfminer.six** – To extract text from PDF resumes
- **python-docx** – To extract text from DOCX files
- **nltk** – For NLP tasks like:
  - Stopword removal
  - Word tokenization
  - Stemming (PorterStemmer)
- **uuid & os** – For safely handling temp file generation

---


---

## 📦 Installation

### Backend

cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload


### Frontend
cd frontend
npm install
npm run dev   # or npm start

