from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Import AI agent function
from ..ai_agent import get_response_from_ai_agent

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str = ""
    messages: List[str]
    allow_search: bool = False

ALLOWED_MODEL_NAMES = [
    "llama3-70b-8192",
    "mixtral-8x7b-32768",
    "llama-3.3-70b-versatile",
    "gpt-4o-mini",
]

app = FastAPI(title="LangGraph AI Agent Backend")

@app.post("/api/chat")
def chat_endpoint(request: RequestState):
    """Chat endpoint that validates input and forwards to the AI agent.
    Returns a JSON object with either `response` or `error` key.
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Please select a valid AI model."}

    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider

    try:
        response = get_response_from_ai_agent(
            llm_id, query, allow_search, system_prompt, provider
        )
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}