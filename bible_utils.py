import requests
from deep_translator import GoogleTranslator

# Supported Bible translations
VERSIONS = {
    "en": "kjv",
    "fr": "lsg",
    "rw": "kir"
}

# Fetch verse text from bible-api.com
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

# Dummy explanation + language translation
def explain_verse(verse_text, lang="en"):
    try:
        explanation = f"This verse means: {verse_text.strip()[:100]}..."
        if lang == "fr":
            return GoogleTranslator(source='auto', target='fr').translate(explanation)
        elif lang == "rw":
            return GoogleTranslator(source='auto', target='rw').translate(explanation)
        return explanation
    except Exception as e:
        return f"Error explaining verse: {e}"
