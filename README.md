# GenAI Multi-Agent Hub

A professional educational project built with Flask, LangChain, Pydantic, and OpenRouter. The application demonstrates how multiple specialized AI agents can be combined into a single interactive workspace with structured JSON outputs.

This project was created as a portfolio implementation inspired by the Coursera course **Develop Generative AI Applications: Get Started**.

## Overview

GenAI Multi-Agent Hub provides one interface for switching between three specialized agents:

- **Support Agent**: Analyzes customer messages, classifies issues, detects sentiment, and suggests a professional response.
- **Marketing Agent**: Converts source content into structured marketing copy for social media and promotional use.
- **Programming Tutor Agent**: Explains programming errors through analysis, hints, concepts, and follow-up questions.

Each agent has its own prompt and Pydantic output schema while sharing the same OpenRouter-compatible language model configuration.

## Features

- Flask web application with a responsive interface.
- Three specialized AI agents in one application.
- Agent switching without leaving the workspace.
- OpenRouter integration through the OpenAI-compatible API.
- LangChain `PromptTemplate` pipelines.
- Structured responses using Pydantic models and `JsonOutputParser`.
- Centralized model configuration.
- Separate modules for each agent.
- JSON API endpoint for programmatic access.
- Automated tests with pytest.
- MIT licensed and ready for GitHub portfolio use.

## Agent Output Schemas

### Support Agent

```text
summary
category
sentiment
response
next_step
```

### Marketing Agent

```text
summary
hook
twitter_post
linkedin_post
call_to_action
```

### Programming Tutor Agent

```text
language
error_analysis
hint
concept
next_question
```

## Technology Stack

- Python 3.10+
- Flask
- LangChain
- LangChain OpenAI
- Pydantic
- OpenRouter
- HTML, CSS, and JavaScript
- pytest

## Project Structure

```text
.
├── agents/
│   ├── __init__.py
│   ├── marketing_agent.py
│   ├── support_agent.py
│   └── tutor_agent.py
├── static/
│   ├── script.js
│   └── styles.css
├── templates/
│   └── index.html
├── tests/
│   └── test_app.py
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
├── app.py
├── config.py
├── model.py
└── requirements.txt
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/774Yk/genai-multi-agent-hub.git
cd genai-multi-agent-hub
```

### 2. Create a virtual environment

#### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

#### Linux or macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure OpenRouter

Set the required environment variables in the same terminal session used to start the application.

#### Windows PowerShell

```powershell
$env:OPENROUTER_API_KEY="your-openrouter-api-key"
$env:OPENROUTER_MODEL="openai/gpt-oss-20b"
$env:OPENROUTER_BASE_URL="https://openrouter.ai/api/v1"
```

#### Linux or macOS

```bash
export OPENROUTER_API_KEY="your-openrouter-api-key"
export OPENROUTER_MODEL="openai/gpt-oss-20b"
export OPENROUTER_BASE_URL="https://openrouter.ai/api/v1"
```

Never commit a real API key to GitHub. The `.env.example` file is provided as a configuration reference only.

## Running the Application

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

## Health Check

The application provides a health endpoint:

```text
http://127.0.0.1:5000/health
```

Expected response:

```json
{
  "status": "ok",
  "agents": [
    "support",
    "marketing",
    "tutor"
  ]
}
```

## API Usage

Send a request to the `/generate` endpoint:

```bash
curl -X POST http://127.0.0.1:5000/generate \
  -H "Content-Type: application/json" \
  -d '{"agent":"support","message":"I was charged twice and need help."}'
```

Valid agent values are:

```text
support
marketing
tutor
```

## Running Tests

From the project root, run:

```bash
pytest -q
```

On Windows PowerShell, if required:

```powershell
$env:PYTHONPATH="."
pytest -q
```

## Security Notes

- Keep `OPENROUTER_API_KEY` outside the source code.
- Do not commit `.env` files or private credentials.
- Rotate an API key immediately if it is accidentally exposed.
- Use environment variables or a secure secrets manager in production.

## Developer

- **Name:** Yassen
- **Email:** [yassenalhajere@gmail.com](mailto:yassenalhajere@gmail.com)
- **LinkedIn:** [linkedin.com/in/yassen-al-hajere-572427387](https://www.linkedin.com/in/yassen-al-hajere-572427387/)

## License

Copyright © 2026 Yassen.

This project is available under the [MIT License](LICENSE).
