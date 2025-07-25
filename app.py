
import streamlit as st
from openai import OpenAI

st.title("SIS-KI Demo – Strukturierte Informationssammlung")

api_key = st.text_input("🔑 OpenAI API Key", type="password")
client = OpenAI(api_key=api_key) if api_key else None

st.markdown("🧠 Gib stichwortartig Beobachtungen oder Einschätzungen zu einem SIS-Themenfeld ein (z. B. 'Mobilität: Rollstuhl, Sturzangst')")

spoken_text = st.text_area("📝 SIS-Stichworte", height=200)

if st.button("📄 Strukturierte Einschätzung generieren") and api_key and spoken_text:
    with st.spinner("KI formuliert professionellen Text..."):
        prompt = f'''
Du bist eine examinierte Pflegefachkraft. Formuliere auf Basis folgender Stichworte eine fachlich korrekte Einschätzung gemäß Strukturierter Informationssammlung (SIS):

"""{spoken_text}"""

Beziehe dich ausschließlich auf die Beschreibung der aktuellen pflegerischen Situation (kein Pflegeziel, keine Maßnahme). Verwende professionelle Sprache und vollständige Sätze.
'''

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Du bist eine Pflegefachkraft und formulierst nach SIS-Struktur."},
                {"role": "user", "content": prompt}
            ]
        )
        pflegeeinschaetzung = response.choices[0].message.content
        st.subheader("📄 Fachliche Einschätzung nach SIS")
        st.text_area("Ergebnis", pflegeeinschaetzung, height=400)
