# First LLM App

Learning project for LLM engineering using the Groq API and Llama 3.

## What it does

A collection of Python scripts exploring core LLM engineering concepts — from basic API calls to RAG pipelines.

## Scripts

### Raw Groq API
- `main.py` — First LLM API call
- `chatbot.py` — Conversational chatbot with memory using conversation history
- `structured.py` — Structured JSON output extraction from text
- `prompt_engineering.py` — Comparison of bad vs good prompts
- `error_handling.py` — Handling API errors gracefully with try/except
- `code_reviewer.py` — Interactive CLI tool that reviews Python code and suggests improvements

### LangChain
- `langchain_intro.py` — LangChain basics: ChatGroq, invoke, SystemMessage/HumanMessage
- `prompt_template.py` — Dynamic prompt templates with variables using ChatPromptTemplate
- `output_parsers.py` — Parsing model output with StrOutputParser and LCEL chains

### Embeddings & RAG
- `embeddings_intro.py` — Text embeddings with HuggingFace, Chroma vector DB, semantic search
- `rag_intro.py` — RAG pipeline: document retrieval + LLM generation with context

## Tech Stack

- Python 3.14
- Groq API (Llama 3.3-70B)
- LangChain + langchain-groq
- HuggingFace sentence-transformers (all-MiniLM-L6-v2)
- Chroma vector database
- python-dotenv

## Setup

1. Clone the repo
2. Create virtual environment: `python3 -m venv venv`
3. Activate: `source venv/bin/activate`
4. Install dependencies: `pip install groq python-dotenv langchain langchain-groq langchain-chroma langchain-huggingface sentence-transformers`
5. Create `.env` file with your Groq API key: `GROQ_API_KEY=your_key_here`
6. Run any script: `python main.py`

## Usage — Code Reviewer

```bash
python code_reviewer.py
```

Paste your Python code and press Enter twice to get a review.