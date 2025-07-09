import streamlit as st
from bible_utils import get_verse, explain_verse

st.set_page_config(page_title="📖 Bible Chatbot", layout="centered")
st.title("📖 Multilingual Bible Chatbot Developed by Gilbert N")

reference = st.text_input("Enter a Bible Verse (e.g., John 3:16)")

if reference:
    st.info(f"Searching for: {reference}")
    cols = st.columns(3)
    languages = [("English", "en"), ("French", "fr"), ("Kinyarwanda", "rw")]

    for col, (lang_name, lang_code) in zip(cols, languages):
        with col:
            st.subheader(lang_name)
            verse = get_verse(reference, lang=lang_code)
            explanation = explain_verse(verse, lang=lang_code)

            st.text_area("Verse", verse, height=100)
            st.text_area("Explanation", explanation, height=150)
