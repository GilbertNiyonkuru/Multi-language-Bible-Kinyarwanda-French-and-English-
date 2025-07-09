import requests
import google.generativeai as genai
from deep_translator import GoogleTranslator
import os
from dotenv import load_dotenv

# Load your Gemini API key from the .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Supported Bible translations
VERSIONS = {
    "en": "kjv",   # King James Version
    "fr": "lsg",   # Louis Segond
    "rw": "kir"    # Kinyarwanda
}

# Get the Bible verse text from bible-api.com
def get_verse(reference, lang="en"):
    try:
        version = VERSIONS.get(lang, "kjv")
        url = f"https://bible-api.com/{reference}?translation={version}"
