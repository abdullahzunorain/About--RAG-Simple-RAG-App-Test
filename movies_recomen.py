import os
import streamlit as st
from groq import Groq

# Configure Streamlit app settings
st.set_page_config(page_title="Movie Recommendation Chatbot", layout="centered")

# Title and intro with styling
st.markdown("<h1 style='text-align: center; color: #FF6347;'>🎬 Movie Recommendation Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Tell me about your favorite genres, actors, or movies you enjoyed, and I'll recommend something you'll like!</p>", unsafe_allow_html=True)

# API key setup: Retrieve the Groq API key from environment variables
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("Error: API Key not found. Please set the GROQ_API_KEY environment variable.")
    st.stop()

# Initialize the Groq client
client = Groq(api_key=api_key)

# Function to get recommendations from Groq API
def get_movie_recommendation(user_input):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"I want a movie recommendation. {user_input}",
                }
            ],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

# Store chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Streamlit UI for chatbot interaction
user_input = st.text_input("You:", placeholder="Describe your movie preferences here...", label_visibility="collapsed")

# If the user provides input, fetch a recommendation
if user_input:
    response = get_movie_recommendation(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.session_state.chat_history.append({"role": "bot", "content": response})

# Display chat history
st.markdown("<div style='height: 400px; overflow-y: auto; border: 1px solid #ddd; padding: 10px; background-color: #F9F9F9;'>", unsafe_allow_html=True)
for message in st.session_state.chat_history:
    if message["role"] == "user":
        st.markdown(f"<div style='text-align: right; color: #333; padding: 10px; background-color: #D3D3D3; border-radius: 10px; margin: 5px 0;'>{message['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align: left; color: #333; padding: 10px; background-color: #FFDDC1; border-radius: 10px; margin: 5px 0;'>{message['content']}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Style adjustments
st.markdown("""
<style>
input {
    font-size: 16px;
    padding: 10px;
    width: 100%;
    border-radius: 8px;
    border: 1px solid #ccc;
    margin-bottom: 10px;
}
.stButton button {
    font-size: 16px;
    background-color: #FF6347;
    color: white;
    padding: 8px 16px;
    border-radius: 8px;
    margin-top: 10px;
}
.stButton button:hover {
    background-color: #FF4500;
}
div[data-testid="stTextInput"] label {
    font-size: 0;
}
</style>
""", unsafe_allow_html=True)




# # app.py

# import os
# import streamlit as st
# from groq import Groq

# # Configure Streamlit app settings
# st.set_page_config(page_title="Movie Recommendation Chatbot", layout="centered")

# # Title and intro
# st.title("🎬 Movie Recommendation Chatbot")
# st.write("Tell me about your favorite genres, actors, or movies you enjoyed, and I'll recommend something you'll like!")

# # API key setup: Retrieve the Groq API key from environment variables
# api_key = os.getenv("GROQ_API_KEY")
# if not api_key:
#     st.error("Error: API Key not found. Please set the GROQ_API_KEY environment variable.")
#     st.stop()

# # Initialize the Groq client
# client = Groq(api_key=api_key)

# # Function to get recommendations from Groq API
# def get_movie_recommendation(user_input):
#     try:
#         chat_completion = client.chat.completions.create(
#             messages=[
#                 {
#                     "role": "user",
#                     "content": f"I want a movie recommendation. {user_input}",
#                 }
#             ],
#             model="llama3-8b-8192",
#         )
#         return chat_completion.choices[0].message.content
#     except Exception as e:
#         return f"An error occurred: {e}"

# # Streamlit UI for chatbot interaction
# user_input = st.text_input("You:", placeholder="Describe your movie preferences here...")

# # If the user provides input, fetch a recommendation
# if user_input:
#     response = get_movie_recommendation(user_input)
#     st.text_area("Chatbot:", value=response, height=200, max_chars=None)

# # Style adjustments
# st.markdown("""
# <style>
# input {font-size: 16px;}
# textarea {font-size: 16px; background-color: #F0F2F6; color: #333333;}
# </style>
# """, unsafe_allow_html=True)
