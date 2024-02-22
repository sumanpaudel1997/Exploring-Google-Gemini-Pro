import os

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

# load gemini to answer question
def get_gemini(question: str):
    response = model.generate_content(question)
    return response.text


st.set_page_config(page_title='Suman"s Gemini Q&A Bot')
st.header('Gemini Pro in Action')

input_qa = st.text_input('Input: ', key='input')
submit = st.button('Ask Gemini')

# after submit
if submit:
    response = get_gemini(input_qa)
    st.subheader("Your Answer:")
    st.write(response)