# 📖 Multilingual Bible Chatbot

This is a simple multilingual Bible chatbot built with **Streamlit**. It fetches Bible verses from [bible-api.com](https://bible-api.com) and provides simple explanations translated into English, French, and Kinyarwanda.

---

## Features

- Enter any Bible verse reference (e.g., John 3:16)
- View the verse text in English (KJV), French (Louis Segond), and Kinyarwanda
- Get a basic explanation of the verse, translated into the selected languages
- Clean, responsive UI using Streamlit

---

## How to use

1. Open the app on [Streamlit Community Cloud](https://streamlit.io/cloud) (deployed version)
2. Type a Bible verse reference in the input box (e.g., `Psalm 23:1`)
3. See the verse and explanation displayed side-by-side in English, French, and Kinyarwanda

---

## Technologies

- Python 3.x
- [Streamlit](https://streamlit.io)
- [bible-api.com](https://bible-api.com) for Bible verse data
- [deep-translator](https://github.com/nidhaloff/deep-translator) for language translation

---

## Setup & Deployment

The app is deployed on Streamlit Community Cloud. To run locally:

1. Clone this repository
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
