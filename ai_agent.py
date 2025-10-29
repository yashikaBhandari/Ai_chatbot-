# ===============================
# 🧠 AI Agent Logic (LangGraph + OpenAI + Groq)
# ===============================

from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
try:
    from langchain_community.tools.ddg_search import DuckDuckGoSearchRun
except Exception:
    # Import may fail in some environments if the underlying dependency
    # (duckduckgo-search) isn't installed. We'll handle initialization
    # lazily so the module import doesn't crash the app during startup.
    DuckDuckGoSearchRun = None
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Lazy search tool initializer. Some hosting environments (like Streamlit
# Cloud) may not have the optional `duckduckgo-search` dependency installed
# at import-time. We create the tool only when a request asks for web search.
search_tool = None

def get_search_tool():
    """Return a DuckDuckGoSearchRun instance or None if unavailable.

    This is lazy and will catch initialization errors so imports don't fail.
    """
    global search_tool
    if search_tool is not None:
        return search_tool
    if DuckDuckGoSearchRun is None:
        return None
    try:
        search_tool = DuckDuckGoSearchRun(name="duckduckgo_search")
        return search_tool
    except Exception as e:
        # Don't raise here — return None and allow the agent to run without search.
        print(f"Warning: DuckDuckGoSearchRun unavailable: {e}")
        search_tool = None
        return None

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

    # Step 3: Decide tools based on allow_search (create lazily)
    tools = []
    if allow_search:
        ddg = get_search_tool()
        if ddg is not None:
            tools.append(ddg)

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