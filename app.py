import streamlit as st
from utils import detect_language, get_bible_explanation  # You can inline these functions if not using utils.py

st.set_page_config(page_title="Bible Helper", layout="centered")
st.title("📖 Multilingual Bible Explanation Bot")

query = st.text_input("Enter a Bible verse or topic (in English, French, or Kinyarwanda):")

if st.button("Explain"):
    if query:
        lang = detect_language(query)
        st.info(f"Detected Language: {lang}")
        with st.spinner("Explaining..."):
            explanation = get_bible_explanation(query, lang)
            st.success("Here is the explanation:")
            st.markdown(explanation)
    else:
        st.warning("Please enter a verse or topic.")
