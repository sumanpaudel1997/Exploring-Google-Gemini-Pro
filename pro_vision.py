import os

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-pro-vision')

# load gemini to answer question


def get_gemini(prompt: str, image):
    if prompt:
        response = model.generate_content([prompt, image])

    response = model.generate_content(image)

    return response.text


st.set_page_config(page_title='Suman"s Gemini Vision Bot')
st.header('Gemini Pro Vision in Action')
input_qa = st.text_input('Input: ', key='input')


# upload file in streamlit app
uploaded_file = st.file_uploader('Upload an Image:', type=['jpeg', 'jpg', 'png'])
image = ''

if not uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image=image, caption='Your Uplaoded Image.', use_column_width=True)

submit = st.button('Tell me about the image')

# after submit
if submit:
    response = get_gemini(prompt=input_qa, image=image)
    st.subheader("Your Answer:")
    st.write(response)
