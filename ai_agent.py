# ===============================
# 🧠 AI Agent Logic (LangGraph + OpenAI + Groq)
# ===============================

from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langchain_community.tools.ddg_search import DuckDuckGoSearchRun
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Step 1: Initialize the Search Tool (✅ updated version)
search_tool = DuckDuckGoSearchRun(name="duckduckgo_search")

# Step 2: Main function to handle AI responses
def get_response_from_ai_agent(model_name, query, allow_search, system_prompt, provider):
    """
    Dynamically create and run an AI Agent using OpenAI or Groq models.
    """

    # Choose provider
    if provider.lower() == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        llm = ChatOpenAI(model=model_name, api_key=api_key)
    elif provider.lower() == "groq":
        api_key = os.getenv("GROQ_API_KEY")
        llm = ChatGroq(model=model_name, api_key=api_key)
    else:
        raise ValueError("Invalid provider! Please choose 'OpenAI' or 'Groq'.")

    # Step 3: Decide tools based on allow_search
    tools = [search_tool] if allow_search else []

    # Step 4: Create the LangGraph ReAct Agent
    agent = create_react_agent(llm, tools)

    # Step 5: Build the messages list with system prompt and user query
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})

    # Add the user query (joining multiple messages if needed)
    user_content = " ".join(query) if isinstance(query, list) else query
    messages.append({"role": "user", "content": user_content})

    # Step 6: Run the agent safely
    try:
        response = agent.invoke({"messages": messages})
        if not response or "messages" not in response:
            return "⚠️ No response received from the agent"
        return response["messages"][-1].content
    except Exception as e:
        error_msg = str(e)
        if "API key" in error_msg:
            return "⚠️ API key error. Please check your environment variables."
        elif "Rate limit" in error_msg:
            return "⚠️ Rate limit reached. Please try again in a moment."
        else:
            return f"⚠️ Agent Error: {error_msg}"