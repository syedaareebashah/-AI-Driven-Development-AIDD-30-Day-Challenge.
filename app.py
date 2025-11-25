import streamlit as st
import PyPDF2
import google.generativeai as genai
import os

# Configure the Gemini API
try:
    # Attempt to get the API key from secrets
    api_key = st.secrets["GEMINI_API_KEY"]
except (KeyError, FileNotFoundError):
    # Fallback to a manually set key if secrets.toml doesn't exist or key is not found
    # This is useful for local development without Streamlit Cloud
    api_key = "AIzaSyAieKO2dATBvC5ifTFy3xA6WmrmfwDpN_I" # Replace with your actual key if not using secrets

genai.configure(api_key=api_key)

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to generate summary using Gemini
def generate_summary(text):
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(f"Summarize the following text:\n\n{text}")
    return response.text

# Function to generate quiz using Gemini
def generate_quiz(text):
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(f"Create a 5-question multiple-choice quiz based on the following text. Include the correct answer for each question:\n\n{text}")
    return response.text

# Streamlit App
st.title("Study Notes Summarizer & Quiz Generator")

uploaded_file = st.file_uploader("Upload your PDF notes", type="pdf")

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully!")
    
    # Extract text from PDF
    with st.spinner("Extracting text from PDF..."):
        document_text = extract_text_from_pdf(uploaded_file)
    st.success("Text extracted!")

    # Generate and display summary
    if "summary" not in st.session_state:
        st.session_state.summary = None
    
    if st.button("Generate Summary"):
        with st.spinner("Generating summary..."):
            st.session_state.summary = generate_summary(document_text)
    
    if st.session_state.summary:
        st.subheader("Summary")
        st.write(st.session_state.summary)

    # Generate and display quiz
    if "quiz" not in st.session_state:
        st.session_state.quiz = None

    if st.button("Create Quiz"):
        with st.spinner("Generating quiz..."):
            st.session_state.quiz = generate_quiz(document_text)

    if st.session_state.quiz:
        st.subheader("Quiz")
        st.write(st.session_state.quiz)
