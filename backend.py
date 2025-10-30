# ===============================
# 🌐 LangGraph AI Agent Backend
# ===============================

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Import AI agent function
from ai_agent import get_response_from_ai_agent


class RequestState(BaseModel):
    model_name: str           # e.g. "gpt-4o-mini" or "llama3-70b-8192"
    model_provider: str       # e.g. "openai" or "groq"
    system_prompt: str = ""   # Optional: system-level instruction
    messages: List[str]       # Chat history or query messages
    allow_search: bool = False    # Whether search tools are enabled


ALLOWED_MODEL_NAMES = [
    "llama3-70b-8192",
    "mixtral-8x7b-32768",
    "llama-3.3-70b-versatile",
    "gpt-4o-mini",
]


app = FastAPI(title="LangGraph AI Agent Backend")


@app.post("/chat")
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


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 9999))
    uvicorn.run(app, host="0.0.0.0", port=port)
# ===============================
# 🌐 LangGraph AI Agent Backend
# ===============================

# Step 1: Import dependencies
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Step 2: Import the function that talks to AI model
from ai_agent import get_response_from_ai_agent

# Step 3: Define schema for incoming requests
class RequestState(BaseModel):
    model_name: str           # e.g. "gpt-4o-mini" or "llama3-70b-8192"
    model_provider: str       # e.g. "openai" or "groq"
    system_prompt: str        # Optional: system-level instruction
    messages: List[str]       # Chat history or query messages
    allow_search: bool        # Whether search tools are enabled

# Step 4: Allowed model names for safety
ALLOWED_MODEL_NAMES = [
    "llama3-70b-8192",
    "mixtral-8x7b-32768",
    "llama-3.3-70b-versatile",
    "gpt-4o-mini"
]

# Step 5: Initialize FastAPI app
app = FastAPI(title="LangGraph AI Agent Backend")

# Step 6: Create API endpoint
@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    Chat endpoint that takes a model name, system prompt,
    messages, and an allow_search flag to get a response
    from the AI Agent dynamically.
    """

    # Validate model name
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Please select a valid AI model."}

    # Extract data from request
    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider

    try:
        # Call AI Agent function
        response = get_response_from_ai_agent(
            llm_id, query, allow_search, system_prompt, provider
        )
        return {"response": response}
    except Exception as e:
        # Catch any runtime errors
        return {"error": str(e)}

# Step 7: Run app (for development)
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 9999))
    uvicorn.run(app, host="0.0.0.0", port=port)
