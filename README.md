# 🤖  AI  Chatbot Agent

A powerful AI chatbot application that combines FastAPI, Streamlit, and LangGraph to create an interactive AI agent with web search capabilities. The application supports multiple AI models from providers like OpenAI and Groq.

## 🌟 Features

- 🎯 Multiple AI model support (OpenAI and Groq)
- 🔍 Web search integration using DuckDuckGo
- 🎨 Clean and intuitive Streamlit UI
- 🚀 Fast and efficient FastAPI backend
- 💡 Customizable system prompts
- ⚡ Real-time responses
- 🛡️ Error handling and input validation

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- OpenAI API key (for OpenAI models)
- Groq API key (for Groq models)

## 🔧 Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd langraph_agent
```

2. **Set up a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install fastapi uvicorn python-dotenv langchain-openai langchain-groq langgraph langchain-community streamlit requests
```

4. **Configure environment variables**
Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_openai_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

## 🚀 Running the Application

1. **Start the backend server**
```bash
python backend.py
```
The backend will run on http://localhost:9999

2. **Start the frontend (in a new terminal)**
```bash
streamlit run frontend.py
```
The frontend will be accessible at http://localhost:8501

## 💻 Usage

1. **Access the web interface**
   - Open your browser and go to http://localhost:8501

2. **Configure your AI Agent**
   - Enter a system prompt (optional)
   - Select your preferred AI provider (OpenAI or Groq)
   - Choose a specific model from the dropdown
   - Enable/disable web search functionality

3. **Start chatting**
   - Enter your query in the text area
   - Click "🚀 Ask Agent!" to get a response
   - View the formatted response in the UI

## 📁 Project Structure

```
langraph_agent/
├── frontend.py      # Streamlit UI implementation
├── backend.py       # FastAPI server implementation
├── ai_agent.py      # AI agent logic and LangGraph integration
├── .env            # Environment variables (create this)
└── README.md       # Project documentation
```

## 🔐 Supported Models

### Groq Models
- llama-3.3-70b-versatile
- mixtral-8x7b-32768

### OpenAI Models
- gpt-4o-mini

## ⚙️ Configuration Options

- **System Prompt**: Custom instructions for the AI agent
- **Model Selection**: Choose between different AI models
- **Provider Selection**: Switch between OpenAI and Groq
- **Web Search**: Toggle DuckDuckGo search integration

## 🛟 Troubleshooting

1. **API Key Errors**
   - Ensure your API keys are correctly set in the `.env` file
   - Verify the API keys are valid and have sufficient credits

2. **Connection Issues**
   - Check if both backend and frontend servers are running
   - Verify the correct ports (9999 for backend, 8501 for frontend) are available

3. **Package Issues**
   - Make sure all dependencies are installed correctly
   - Use the virtual environment when running the application

## 📝 Notes

- The backend uses FastAPI for efficient API handling
- Web search is performed using DuckDuckGo
- The frontend is built with Streamlit for easy interaction
- Error handling is implemented throughout the application

## 🔒 Security

- API keys are managed through environment variables
- Input validation is implemented on both frontend and backend
- Model names are validated against an allowed list

## 🤝 Contributing

Feel free to:
- Submit bug reports
- Propose new features
- Submit pull requests

## 🌐 Deployment

This project is deployed using [Streamlit Cloud](https://streamlit.io/cloud). The application runs as a single service with integrated AI functionality.

### Deployment Files

1. **requirements.txt**: All Python dependencies with specific versions
2. **.streamlit/secrets.toml**: Configuration for API keys (create from .env.example)
3. **frontend.py**: Main Streamlit application

### Deployment Steps

1. **Prepare for Deployment**
   - Ensure all files are committed to GitHub
   - Create a free account on [Streamlit Cloud](https://streamlit.io/cloud)
   - Create `.streamlit/secrets.toml` with your API keys (don't commit this file)

2. **Deploy on Streamlit Cloud**
   - Connect your GitHub repository
   - Select the `frontend.py` file
   - Add your secrets in the Streamlit Cloud dashboard:
     - `OPENAI_API_KEY`
     - `GROQ_API_KEY`
   - Deploy the application

3. **Post Deployment**
   - Your app will be available at `https://your-app-name.streamlit.app`
   - Test the application thoroughly
   - Share the URL with others

### Environment Variables

```env
OPENAI_API_KEY=your_openai_api_key_here
GROQ_API_KEY=your_groq_api_key_here
BACKEND_URL=your_backend_url_here  # Required for deployed frontend
```

### Deployment Considerations

- Free tier limitations on Render
- Service spin-down after 15 minutes of inactivity
- Initial cold start might be slow
- Monitor usage and logs in Render dashboard

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.