import json

def load_bible(language_code):
    filename = {
        'en': 'bible_en.json',
        'fr': 'bible_fr.json',
        'rw': 'bible_rw.json'
    }.get(language_code, 'bible_en.json')

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}
