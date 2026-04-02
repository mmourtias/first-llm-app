# First LLM App

Learning project for LLM engineering using the Groq API and Llama 3.

## What it does

A collection of Python scripts exploring core LLM engineering concepts.

## Scripts

- `main.py` — First LLM API call
- `chatbot.py` — Conversational chatbot with memory using conversation history
- `structured.py` — Structured JSON output extraction from text
- `prompt_engineering.py` — Comparison of bad vs good prompts
- `error_handling.py` — Handling API errors gracefully with try/except

## Tech Stack

- Python 3.11
- Groq API (Llama 3.3-70B)
- python-dotenv

## Setup

1. Clone the repo
2. Create virtual environment: `python3 -m venv venv`
3. Activate: `source venv/bin/activate`
4. Install dependencies: `pip install groq python-dotenv`
5. Create `.env` file with your Groq API key: `GROQ_API_KEY=your_key_here`
6. Run any script: `python main.py`
