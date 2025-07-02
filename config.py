# config.py
import streamlit as st
import google.generativeai as genai
import os

# Mengatur Google Gemini API Key
try:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"] or os.getenv("GOOGLE_API_KEY")
except (KeyError, TypeError):
    st.error("Google Gemini API key not found in Streamlit Secrets or environment variable.")
    st.stop()

# Function to get the configured Gemini model
def get_gemini_model():
    genai.configure(api_key=GOOGLE_API_KEY)
    return genai.GenerativeModel('gemini-2.5-flash')