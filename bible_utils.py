import requests
from deep_translator import GoogleTranslator

def get_verse(reference, lang="en"):
    try:
        # Always get English verse
        url = f"https://bible-api.com/{reference}?translation=kjv"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        verse_text = data.get("text", "Verse not found.")
        
        # Translate verse if not English
        if lang != "en":
            try:
                verse_text = GoogleTranslator(source='en', target=lang).translate(verse_text)
            except Exception:
                verse_text += " (Translation unavailable)"
        
        return verse_text
    except Exception as e:
        return f"Error fetching verse: {e}"

def explain_verse(verse_text, lang="en"):
    try:
        explanation = f"This verse means: {verse_text.strip()}"
        if lang != "en":
            try:
                explanation = GoogleTranslator(source='en', target=lang).translate(explanation)
            except Exception:
                explanation += " (Translation unavailable)"
        return explanation
    except Exception as e:
        return f"Error explaining verse: {e}"
