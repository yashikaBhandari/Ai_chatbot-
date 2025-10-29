# ===============================
# 🎨 LangGraph AI Agent Frontend (Streamlit)
# ===============================

import streamlit as st
import requests
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langchain_community.tools.ddg_search import DuckDuckGoSearchRun
import os

# Initialize the Search Tool
search_tool = DuckDuckGoSearchRun(name="duckduckgo_search")

# Load API keys from Streamlit secrets in production, or environment variables in development
def get_api_key(key_name):
    try:
        return st.secrets[key_name]
    except:
        return os.getenv(key_name)

OPENAI_API_KEY = get_api_key("OPENAI_API_KEY")
GROQ_API_KEY = get_api_key("GROQ_API_KEY")

# Initialize AI function
def get_ai_response(model_name, query, allow_search, system_prompt, provider):
    # Choose provider
    if provider.lower() == "openai":
        llm = ChatOpenAI(model=model_name, api_key=OPENAI_API_KEY)
    elif provider.lower() == "groq":
        llm = ChatGroq(model=model_name, api_key=GROQ_API_KEY)
    else:
        raise ValueError("Invalid provider!")

    # Set up tools
    tools = [search_tool] if allow_search else []

    # Create the agent
    agent = create_react_agent(llm, tools)

    # Prepare messages
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})

    messages.append({"role": "user", "content": query})

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

# Page setup
st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("🤖 AI Chatbot Agents")
st.write("Create and Interact with AI Agents using LangGraph!")

# Step 2: Define inputs
system_prompt = st.text_area(
    "🧠 Define your AI Agent:",
    height=70,
    placeholder="Type your system prompt here..."
)

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select Provider:", ("Groq", "OpenAI"))

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)

allow_web_search = st.checkbox("Allow Web Search")

user_query = st.text_area("💬 Enter your query:", height=150, placeholder="Ask Anything!")

API_URL = "http://127.0.0.1:9999/chat"

# Step 3: Button for sending request
if st.button("🚀 Ask Agent!"):
    if user_query.strip():
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        try:
            # Get response directly from AI function
            response = get_ai_response(
                selected_model,
                user_query,
                allow_web_search,
                system_prompt,
                provider
            )

            st.subheader("🧩 Agent Response")

            # Display the response
            if isinstance(response, str):
                # Convert escaped newlines to actual ones
                response_text = response.replace("\\n", "\n")

                # Display formatted Markdown
                st.markdown(response_text)

                # Also show in a text box
                st.text_area("📜 Full Response", response_text, height=400)
            else:
                st.error("⚠️ Unexpected response format")

        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")
