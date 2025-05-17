import streamlit as st

st.set_page_config(page_title="Groq Chatbot", page_icon=":robot_face:", layout="centered")
st.title("AI Chatbot")
st.write("Chat using Groq AI and Tavily.")
system_prompt = st.text_area("System Prompt",height=70 ,placeholder="Enter your system prompt here...")

MODEL_NAME_GROQS = ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "llama3-70b-8192"]

provider=st.radio("Select Model Provider:", ("Groq"))

if provider == "Groq":
    select_model=st.selectbox("Select Groq Model:", MODEL_NAME_GROQS)
    
allow_search=st.checkbox("Allow Search")

user_query = st.text_area("Chat", height=200, placeholder="Ask  Anything...")

API_URL="https://agentic-chatbot-6n5r.onrender.com/chat"


if st.button("Ask AI"):
    if user_query.strip():
        import requests
        
        # Create a placeholder for loading message
        with st.spinner('Getting response from AI...'):
            payload={
                "model_name": select_model,
                "model_provider": provider,
                "system_prompt": system_prompt,
                "messages": [user_query],
                "allow_search": allow_search
            }
            
            response=requests.post(API_URL, json=payload)
            if response.status_code == 200:
                response_data=response.json()
                if "error" in response_data:
                    st.error(response_data["error"])
                else:
                    st.subheader("Agent Response")
                    st.markdown(f"Answer: {response_data}")