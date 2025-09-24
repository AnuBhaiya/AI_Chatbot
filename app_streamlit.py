# app_streamlit.py
import streamlit as st
from streamlit_chat import message
from chatbot_openai import OpenAIChatbot

st.set_page_config(page_title="Domain Specific Chatbot", layout="centered")
st.title("Domain-Specific AI Chatbot")

if 'chatbot' not in st.session_state:
    medical_prompt = (
        "You are a medical information assistant. Provide general information about health topics, "
        "but always state that you are not a medical professional and users should consult a doctor."
    )
    st.session_state['chatbot'] = OpenAIChatbot(system_prompt=medical_prompt)
if 'history' not in st.session_state:
    st.session_state['history'] = []

# Display existing history
for i, chat in enumerate(st.session_state['history']):
    message(chat['message'], is_user=chat['is_user'], key=f"chat_{i}")

# Input box
user_input = st.text_input("Your message:", key="user_input")
if user_input:
    st.session_state['history'].append({"message": user_input, "is_user": True})
    bot_response = st.session_state['chatbot'].get_response(user_input)
    st.session_state['history'].append({"message": bot_response, "is_user": False})
    # rerun to display new messages
    st.experimental_rerun()
