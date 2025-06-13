import re
from collections import Counter
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Ensure nltk resources are available
try:
    stop_words = set(stopwords.words("english"))
except LookupError:
    nltk.download("stopwords")
    stop_words = set(stopwords.words("english"))

try:
    word_tokenize("test")
except LookupError:
    nltk.download("punkt_tab")

stemmer = PorterStemmer()

def clean_and_stem(text):
    text = re.sub(r"[^a-zA-Z\s]", "", text.lower())
    words = word_tokenize(text)
    return [stemmer.stem(w) for w in words if w not in stop_words and len(w) > 2]

def analyze_keywords(resume_text, job_desc):
    resume_words = clean_and_stem(resume_text)
    job_words = clean_and_stem(job_desc)

    resume_counts = Counter(resume_words)
    job_counts = Counter(job_words)

    keywords = set(job_words)
    missing_keywords = [kw for kw in keywords if kw not in resume_counts]
    matched_keywords = [kw for kw in keywords if kw in resume_counts]

    score = len(matched_keywords) / len(keywords) * 100 if keywords else 0
    return {
        "match_score": round(score, 2),
        "missing_keywords": missing_keywords[:10],
        "matched_keywords": matched_keywords[:10],
    }

# Example usage
if __name__ == "__main__":
    resume = "Experienced software engineer with skills in Python, Java, and machine learning."
    job = "Looking for a software engineer with expertise in Python, Java, and data science."
    print(analyze_keywords(resume, job))
