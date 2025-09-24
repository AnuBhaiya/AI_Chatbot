<<<<<<< HEAD
# AI Project 1: Domain-Specific Chatbot

This repo contains two implementations:
1. API-driven chatbot using OpenAI (chatbot_openai.py + app_streamlit.py)
2. Local RAG chatbot (chatbot_rag_local.py) - requires Ollama and local setup

## Quick start (recommended: VS Code)

1. Create & activate virtual environment
   - Windows (PowerShell):
     ```
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - macOS / Linux:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

2. Install dependencies:
pip install -r requirements.txt


3. Set OPENAI_API_KEY environment variable:
- Windows (PowerShell):
  ```
  setx OPENAI_API_KEY "sk-..."
  ```
  or temporary:
  ```
  $env:OPENAI_API_KEY="sk-..."
  ```
- macOS / Linux:
  ```
  export OPENAI_API_KEY="sk-..."
  ```

4. Run CLI version:

python chatbot_openai.py

5. Run Streamlit UI (recommended):
streamlit run app_streamlit.py


6. Local RAG (advanced): create ./data with docs, run an Ollama server, then:
python chatbot_rag_local.py
=======
# AI_Chatbot
>>>>>>> ff795f60417919736aeacba3980868f8b804a317
