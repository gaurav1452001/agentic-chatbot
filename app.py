import os
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import AI agent dependencies
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

# Define API models
class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str  
    messages: List[str]
    allow_search: bool

# Define allowed models
ALLOWED_MODELS = ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "llama3-70b-8192"]

# AI agent function
def get_ai_response(llm_id, query, allow_search, system_prompt, provider):
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    tools = [TavilySearchResults(max_results=2)] if allow_search else []
 
    agent = create_react_agent(
        model=llm,
        tools=tools,
        state_modifier=system_prompt
    )

    state = {"messages": query}
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_messages = [msg.content for msg in messages if isinstance(msg, AIMessage)]
    return ai_messages[-1]

# Initialize FastAPI app
app = FastAPI(title="AI Agent")

# Define API endpoints
@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    Endpoint to handle chat requests.
    """
    if request.model_name not in ALLOWED_MODELS:
        return {"error": "Model not allowed"}
    
    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider
    
    response = get_ai_response(llm_id, query, allow_search, system_prompt, provider)
    return response

# Add CORS middleware for production
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You should restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route for health checks
@app.get("/")
def read_root():
    return {"status": "ok", "message": "AI Agent API is running"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
