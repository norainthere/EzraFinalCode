import streamlit as st
from audio_uploader import AudioUploader
from audio_analysis.audio_analyzer import AudioAnalyzer
from eq_generator import EQGenerator
from verbal_prompt_processor import VerbalPromptProcessor

# Create instances of your classes
uploader = AudioUploader()
analyzer = AudioAnalyzer()
eq_gen = EQGenerator()
prompt_processor = VerbalPromptProcessor()

# Define your Streamlit interface
st.title("AI EQ Generator")

uploaded_file = st.file_uploader("Choose an audio file")

if uploaded_file is not None:
    audio = uploader.upload(uploaded_file)
    analysis = analyzer.analyze(audio)
    eq = eq_gen.generate(analysis)

    prompt = st.text_input("Enter a descriptive prompt")
    if prompt:
        prompt_analysis = prompt_processor.process(prompt)
        eq = eq_gen.adjust(eq, prompt_analysis)

    st.write("Suggested EQ curve:", eq)
