from pydantic import BaseModel
from typing import List
class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str  
    messages:List[str]
    allow_search: bool
    
from fastapi import FastAPI
from ai_agent import get_ai_response

ALLOWED_MODELS=["llama-3.3-70b-versatile","llama-3.1-8b-instant","llama3-70b-8192"]

app=FastAPI(title="AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    Endpoint to handle chat requests.
    """
    if request.model_name not in ALLOWED_MODELS:
        return {"error": "Model not allowed"}
    
    llm_id=request.model_name
    query=request.messages
    allow_search=request.allow_search
    system_prompt=request.system_prompt
    provider=request.model_provider
    
    response=get_ai_response(llm_id,query,allow_search,system_prompt,provider)
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    