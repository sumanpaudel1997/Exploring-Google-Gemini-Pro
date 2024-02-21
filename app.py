import os

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()


genai.configure(os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

# load gemini to answer question


def get_gemini(question: str):
    response = model.generate_content(question)
    return response.text
