import pytesseract
from pdf2image import convert_from_path
import os

def extract_text_from_pdf(file_path: str) -> str:
    images = convert_from_path(file_path)
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image) + "\n"
    return text