import streamlit as st

st.set_page_config(page_title="Groq Chatbot", page_icon=":robot_face:", layout="wide")
st.title("AI Chatbot")
st.write("Chat using Groq AI and Tavily.")
system_prompt = st.text_area("System Prompt",height=70 ,placeholder="Enter your system prompt here...")

MODEL_NAME_GROQS = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768", "llama3-70b-8192"]

provider=st.radio("Select Model Provider:", ("Groq"))

if provider == "Groq":
    select_model=st.selectbox("Select Groq Model:", MODEL_NAME_GROQS)
    
allow_search=st.checkbox("Allow Search")

user_query = st.text_area("Chat", height=200, placeholder="Ask  Anything...")

if st.button("Ask AI"):
    if user_query.strip():
        response="Hi"