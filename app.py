
import streamlit as st
from openai import OpenAI

st.title("SIS-KI Demo – Pflegeplanung per Spracheingabe")

api_key = st.text_input("🔑 OpenAI API Key", type="password")
client = OpenAI (api_key=api_key) if api_key else None

spoken_text = st.text_area("🎙 Spracheingabe (per WIN + H diktieren)", height=200)

if st.button("🧠 Pflegeplanung generieren") and api_key and spoken_text:
    with st.spinner("KI analysiert..."):
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Du bist ein Pflegeexperte. Erstelle eine Pflegeplanung gemäß den SIS-Themenfeldern."},
                {"role": "user", "content": spoken_text}
            ]
        )
        pflegeplanung = response['choices'][0]['message']['content']
        st.subheader("📄 Pflegeplanung nach SIS")
        st.text_area("Ergebnis", pflegeplanung, height=300)
