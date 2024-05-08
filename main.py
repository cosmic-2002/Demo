import os

import streamlit as st
#from dotenv import load_dotenv
import google.generativeai as gen_ai


# Load environment variables
GOOGLE_API_KEY='AIzaSyCMdVnONomr73BxNv64DhWfbuMxw-QpiK0'

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Danny!",
    page_icon=":raccoon:",  # Favicon emoji
    layout="centered",  # Page layout option
)

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')


# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])


# Display the chatbot's title on the page
st.title("😶‍🌫️ Danny- Bot")

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)
        
prompt =[f'''You are a shy introvert boy who gets very close and attached with close ones,your name is Danny and have few very very close friends like Chirage but u have a very very close friend Archita ''']
def smart(text_input, prompt):
    prompt_parts = [prompt[0], text_input]
    response = model.generate_content(prompt_parts)
    return response

# Input field for user's message
user_prompt = st.chat_input("Ask anything miss...")
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
