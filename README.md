# AI Chatbot Agent

This is an AI chatbot agent that uses Groq AI models with optional Tavily search integration.

## Project Structure

- `app.py` - Combined backend and AI agent functionality for deployment
- `frontend.py` - Streamlit frontend for local development
- `requirements.txt` - Dependencies for deployment
- `Procfile` - Instructions for Render deployment

## Deployment on Render

1. Sign up or log in to [Render](https://render.com/)
2. Create a new Web Service
3. Connect your GitHub repository
4. Set the following configuration:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app:app --host=0.0.0.0 --port=$PORT`
   - **Environment Variables:**
     - `GROQ_API_KEY`: Your Groq API key
     - `TAVILY_API_KEY`: Your Tavily API key

## Local Development

1. Install dependencies: `pip install -r requirements.txt`
2. Create a `.env` file based on `.env.example`
3. Run the backend: `uvicorn app:app --reload`
4. Run the frontend: `streamlit run frontend.py`

## API Usage

Send a POST request to `/chat` with the following JSON structure:

```json
{
  "model_name": "llama-3.3-70b-versatile",
  "model_provider": "Groq",
  "system_prompt": "Act as a helpful assistant",
  "messages": ["Your query here"],
  "allow_search": true
}
```
