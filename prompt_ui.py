from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st  
load_dotenv()

st.header("Reasearch tool")
user_input=st.text_input("Enter your query here:")

if st.button("Submit"):
    model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.2, max_tokens=100)
    result = model.invoke(user_input)
    st.write(result.content)  # Display the result in the Streamlit app
