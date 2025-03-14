# Doenizer: Medical Notes Anonymizer

Doenizer helps healthcare professionals, medical students, and healthtech innovators anonymize sensitive patient data from medical notes, ensuring compliance with privacy regulations like HIPAA.

## 💡 How Doenizer Works

1. **Speech-to-Text (Deepgram)**: Converts audio notes into text.
2. **NLP Anonymization (spaCy)**: Detects and replaces sensitive information with generic placeholders.

## 🌐 Live Demo

A Live Demo for Doenizer can be found [here](https://doenizer.streamlit.app/)

## 🌐 Getting Started

1. **Clone the repo**:
    ```bash
    git clone https://github.com/yourusername/Doenizer.git
    cd Doenizer
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set API Keys** (Deepgram related for speech-to-text).

4. **Run the app**:
    ```bash
    streamlit run main.py
    ```

## 📑 Example: Anonymized Medical Note

**Original Doctor's Note**:
```
Patient John Doe, a 45-year-old male, complains of persistent headaches for the past two weeks.
The patient reports no history of migraines but mentions recent increased work stress.
No nausea or vomiting. Blood pressure today is 140/90 mmHg.
Neurological exam is unremarkable. No signs of infection or trauma.
Suspected stress-related tension headaches. Recommended stress management techniques
and prescribed ibuprofen 400mg as needed. Follow-up in two weeks if symptoms persist.
```

**Anonymized Doctor's Note**:
```
Patient [PERSON], a [DATE] male, complains of persistent headaches for [DATE].
The patient reports no history of migraines but mentions recent increased work stress.
No nausea or vomiting. Blood pressure [DATE] is 140/90 mmHg.
Neurological exam is unremarkable. No signs of infection or trauma.
Suspected stress-related tension headaches. Recommended stress management techniques
and prescribed ibuprofen 400mg as needed. Follow-up in [DATE] if symptoms persist.
```

## 📦 Technologies

- **Python**
- **Streamlit**
- **Deepgram API (Speech-to-Text)**
- **spaCy (NLP Anonymization)**

## ⚡ Contributing

Fork the repo, make changes, and submit a pull request.

## 🔒 License

MIT License. See [LICENSE](LICENSE).

