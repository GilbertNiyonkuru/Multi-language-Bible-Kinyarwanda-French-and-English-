import requests
from deep_translator import GoogleTranslator

VERSIONS = {
    "en": "kjv",
    "fr": "lsg",
    "rw": "kir"  # Confirm if supported
}

def get_verse(reference, lang="en"):
    try:
        version = VERSIONS.get(lang, "kjv")
        url = f"https://bible-api.com/{reference}?translation={version}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        verse_text = data.get("text", "")

        # If no text returned and lang is rw (Kinyarwanda), fallback to English
        if not verse_text and lang == "rw":
            url_en = f"https://bible-api.com/{reference}?translation=kjv"
            resp_en = requests.get(url_en)
            resp_en.raise_for_status()
            data_en = resp_en.json()
            verse_text = data_en.get("text", "Verse not found.")
        return verse_text if verse_text else "Verse not found."
    except Exception as e:
        return f"Error fetching verse: {e}"

def explain_verse(verse_text, lang="en"):
    try:
        explanation = f"This verse means: {verse_text.strip()}"
        if lang == "fr":
            try:
                return GoogleTranslator(source='auto', target='fr').translate(explanation)
            except Exception:
                return explanation + " (Translation unavailable)"
        elif lang == "rw":
            try:
                return GoogleTranslator(source='auto', target='rw').translate(explanation)
            except Exception:
                return explanation + " (Translation unavailable)"
        return explanation
    except Exception as e:
        return f"Error explaining verse: {e}"
