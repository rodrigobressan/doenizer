import streamlit as st
import requests
import os
from dotenv import load_dotenv
import spacy
from streamlit_option_menu import option_menu

# Load API keys from .env file
load_dotenv()
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")

# Load spaCy model for NER
nlp = spacy.load("en_core_web_sm")


# Function to transcribe audio using Deepgram
def transcribe_audio(audio_bytes):
    headers = {
        "Authorization": f"Token {DEEPGRAM_API_KEY}",
        "Content-Type": "audio/wav"
    }
    response = requests.post("https://api.deepgram.com/v1/listen", headers=headers, data=audio_bytes)
    return response.json().get("results", {}).get("channels", [{}])[0].get("alternatives", [{}])[0].get("transcript",
                                                                                                        "")


# Function to anonymize text using spaCy
def anonymize_text(text):
    doc = nlp(text)
    anonymized_text = text

    # Replace sensitive entities with generic placeholders
    for ent in doc.ents:
        if ent.label_ in ["PERSON", "ORG", "GPE", "DATE", "LOC", "TIME", "NORP", "MONEY"]:
            anonymized_text = anonymized_text.replace(ent.text, f"[{ent.label_}]")

    return anonymized_text


# Streamlit UI Configuration
st.set_page_config(page_title="Doenizer", layout="wide", initial_sidebar_state="expanded")

# Sidebar Navigation with Stylish Option Menu
with st.sidebar:
    page = option_menu(
        menu_title="🥸 Doenizer",
        options=["How It Works", "Example", "Audio Anonymizer", "Text Anonymizer"],
        icons=["info-circle", "book", "mic", "file-text"],
        menu_icon="none",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#f0f2f6"},
            "icon": {"color": "black", "font-size": "20px"},
            "nav-link": {"font-size": "18px", "text-align": "left", "margin": "5px", "color": "#333"},
            "nav-link-selected": {"background-color": "#2E7D32", "color": "white"},
        },
    )

# Upload & Anonymize Page
if page == "Audio Anonymizer":
    st.title("📤 Upload & Anonymize Medical Notes (Audio)")
    st.markdown(
        "Upload an audio file of a doctor's note, and Doenize will transcribe it and anonymize sensitive patient data.")

    uploaded_file = st.file_uploader(
        "Upload your doctor's note (WAV, MP3, M4A)",
        type=["wav", "mp3", "m4a"],
        help="Only audio files are supported."
    )

    if uploaded_file is not None:
        st.audio(uploaded_file, format="audio/wav")

        if st.button("Anonymize Medical Note 🥸", use_container_width=True):
            with st.spinner("Processing..."):
                audio_bytes = uploaded_file.getvalue()
                transcript = transcribe_audio(audio_bytes)
                anonymized_transcript = anonymize_text(transcript)

                st.success("✅ Anonymization complete!")
                st.subheader("📜 Transcript:")
                st.text_area("", transcript, height=150)
                st.subheader("🔒 Anonymized Transcript:")
                st.text_area("", anonymized_transcript, height=200)

# Text Anonymizer Page
elif page == "Text Anonymizer":
    st.title("📝 Text Anonymizer")
    st.markdown(
        "You can also anonymize plain text input. Paste your text below, and our tool will anonymize any sensitive information.")

    text_input = st.text_area("Enter your medical note text here:", height=200)

    if st.button("Anonymize Text 🔒", use_container_width=True):
        if text_input.strip() != "":
            anonymized_text = anonymize_text(text_input)
            st.subheader("🔒 Anonymized Text:")
            st.text_area("", anonymized_text, height=200)
        else:
            st.warning("Please enter some text to anonymize.")

# Example Page
elif page == "Example":
    st.title("📑 Example: Anonymized Medical Note")
    st.markdown("""
        ### Sample Doctor’s Note:
        Below is an example of a **typical medical note**. The tool will anonymize sensitive data, such as the patient’s name and medical details.
    """)

    sample_note = """
    Patient John Doe, a 45-year-old male, complains of persistent headaches for the past two weeks. 
    The patient reports no history of migraines but mentions recent increased work stress. 
    No nausea or vomiting. Blood pressure today is 140/90 mmHg. 
    Neurological exam is unremarkable. No signs of infection or trauma. 
    Suspected stress-related tension headaches. Recommended stress management techniques 
    and prescribed ibuprofen 400mg as needed. Follow-up in two weeks if symptoms persist.
    """

    anonymized_sample = anonymize_text(sample_note)

    st.text_area("📋 Original Doctor’s Note:", sample_note, height=150)
    st.text_area("🔒 Anonymized Doctor’s Note:", anonymized_sample, height=200)

# How It Works Page
elif page == "How It Works":
    st.title("💡 How It Works")
    st.markdown("""
        This tool helps **healthcare professionals, medical students, and healthtech innovators** by anonymizing sensitive patient data from medical notes.

        **Navigate to the 'Upload & Anonymize' page to start using it, or check the 'Example' page to see how it works!**

        **Anonymization process:**
        - **🎙️ Speech-to-Text (Deepgram):** Converts audio notes into text.
        - **🧠 NLP Anonymization (spaCy):** Detects and replaces sensitive information with generic placeholders.

        **Who benefits from this?**
        - 🏥 **Doctors & Nurses**: Secure patient data.
        - 📚 **Medical Students**: Learning the importance of data anonymization.
        - 🚀 **HealthTech Innovators**: Create solutions that comply with privacy regulations like HIPAA.
    """)

# About Page
elif page == "About":
    st.title("📌 About This Project")
    st.markdown("""
        Doenize anonymizes medical notes using **speech recognition** and **natural language processing** to ensure patient privacy.

        - 🎙️ **Deepgram** (Speech-to-Text)  
        - 🧠 **spaCy** (NLP for Entity Recognition & Anonymization)  
        - 🎨 **Streamlit** (UI Framework)

        **Join us in ensuring the security of medical data! 🔒**
    """)
