# 🤖 AI Chatbot Agent

A powerful AI chatbot application built with FastAPI, Streamlit, and LangGraph. Features real-time web search capabilities and supports both OpenAI and Groq models.

## 🌟 Features

- Multiple AI model support (OpenAI and Groq)
- Web search integration
- Clean Streamlit UI
- FastAPI backend
- Customizable system prompts
- Real-time responses

## � Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/yashikaBhandari/Ai_chatbot-.git
cd Ai_chatbot-
```

2. **Set up virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
```

5. **Run the application**

In one terminal (Backend):
```bash
python backend.py
```

In another terminal (Frontend):
```bash
streamlit run frontend.py
```

Visit http://localhost:8501 in your browser.

## 💻 Usage

1. Open http://localhost:8501
2. Define your AI agent's behavior using the system prompt
3. Choose your provider (Groq or OpenAI)
4. Select a model:
   - Groq: llama-3.3-70b-versatile or mixtral-8x7b-32768
   - OpenAI: gpt-4o-mini
5. Enable web search if needed
6. Enter your query and click "Ask Agent!"

## 📁 Project Structure

```
Ai_chatbot-/
├── frontend.py    # Streamlit UI
├── backend.py     # FastAPI server
├── ai_agent.py    # AI agent logic
├── .env          # Environment variables (create this)
└── README.md     # Documentation
```

## ⚙️ Environment Variables

Required environment variables in your `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
```

## 🔧 Development

- Backend runs on http://localhost:9999
- Frontend runs on http://localhost:8501
- Uses FastAPI for API endpoints
- Streamlit for user interface
- LangGraph for AI agent functionality

## �️ Troubleshooting

1. **Port already in use**
```bash
# Find the process
lsof -nP -iTCP:9999 -sTCP:LISTEN
# Kill the process
kill <PID>
```

2. **API Key Issues**
- Ensure your `.env` file exists and contains valid API keys
- Verify the API keys have sufficient credits

3. **Dependencies**
- Make sure to activate the virtual environment
- Install all requirements: `pip install -r requirements.txt`

## 📝 Notes

- Keep your API keys secure and never commit them to the repository
- The `.env` file is included in `.gitignore`
- When using web search, ensure you have a stable internet connection