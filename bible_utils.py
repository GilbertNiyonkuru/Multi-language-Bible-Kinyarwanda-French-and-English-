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

# ✅ 1. Get the Bible verse
def get_verse(reference, lang="en"):
    try:
        version = VERSIONS.get(lang, "kjv")
        url = f"https://bible-api.com/{reference}?translation={version}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("text", "Verse not found.")
    except Exception as e:
        return f"Error fetching verse: {e}"

# ✅ 2. Explain the verse using Gemini, with language support
def explain_verse_with_gemini(verse_text, lang="en"):
    try:
        model = genai.GenerativeModel("gemini-pro")
        prompt = f"Explain the following Bible verse in simple terms:\n\n{verse_text}"
        response = model.generate_content(prompt)
        explanation = response.text.strip()

        # Translate if needed
        if lang == "fr":
            return GoogleTranslator(source='auto', target='fr').translate(explanation)
        elif lang == "rw":
            return GoogleTranslator(source='auto', target='rw').translate(explanation)
        else:
            return explanation
    except Exception as e:
        return f"Error generating explanation: {e}"
