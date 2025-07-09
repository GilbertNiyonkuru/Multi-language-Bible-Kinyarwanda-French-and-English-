import streamlit as st
from bible_utils import get_verse, explain_verse_with_gemini

st.set_page_config(page_title="📖 Bible Chatbot with Gemini", layout="centered")
st.title("📖 Multilingual Bible Chatbot")

reference = st.text_input("Enter a Bible Verse (e.g., John 3:16)")

if reference:
    st.info(f"Fetching explanation for: {reference}")
    cols = st.columns(3)
    languages = [("English", "en"), ("French", "fr"), ("Kinyarwanda", "rw")]

    for col, (lang_name, lang_code) in zip(cols, languages):
        with col:
            st.subheader(lang_name)
            verse = get_verse(reference, lang=lang_code)
            explanation = explain_verse_with_gemini(verse, lang=lang_code)

            st.text_area("Verse", verse, height=100)
            st.text_area("Explanation", explanation, height=150)
