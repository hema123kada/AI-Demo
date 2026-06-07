import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model=genai.GenerativeModel("gemini-2.5-flash")
st.title("Gemini AI chatbot")
user_input=st.text_input("ask the question?")
if st.button("Generate Response:"):
    try:
        response=model.generate_content(user_input)
        st.write(response.text)
    except:
        st.error("Quota exceeded.please try later or upgrade your API plan.")