import os
import docx
import textract
from pdfminer.high_level import extract_text as extract_text_pdf

def extract_text_from_pdf(file_path: str) -> str:
    return extract_text_pdf(file_path).strip()

def extract_text_from_doc(file_path: str) -> str:
    try:
        return textract.process(file_path).decode("utf-8").strip()
    except Exception as e:
        return f"Failed to extract .doc text: {str(e)}"

def extract_text_from_docx(file_path: str) -> str:
    try:
        doc = docx.Document(file_path)
        return "\n".join(p.text for p in doc.paragraphs).strip()
    except Exception as e:
        return f"Failed to extract .docx text: {str(e)}"

def extract_text_by_filetype(filename: str, file_bytes: bytes) -> str:
    with open(filename, "wb") as f:
        f.write(file_bytes)

    try:
        if filename.endswith(".pdf"):
            return extract_text_from_pdf(filename)
        elif filename.endswith(".docx"):
            return extract_text_from_docx(filename)
        elif filename.endswith(".doc"):
            return extract_text_from_doc(filename)
        else:
            return "Unsupported file format"
    finally:
        if os.path.exists(filename):
            os.remove(filename)
