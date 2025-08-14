# Agentic AI Demo (Multi‑LLM) 🚀

A modular Python project to demonstrate building and running AI agents with multiple LLM backends. Initially implemented with **Ollama**, this project is designed to expand in the future to include **OpenAI** and other LLM providers. Additionally, the roadmap includes building a **FastAPI** backend to expose these agents as APIs, which can then be consumed by other platforms, such as Android applications.

---

## Project Structure

```
agenticAI-demo/
├── ollama_agent/              # Ollama-based agent implementation
│   ├── __pycache__/           # Python cache files
│   ├── agent_runner.py        # Main runner for Ollama agent tasks
│   ├── config_settings.py     # Configuration for Ollama agent
│   ├── llm_setup.py           # Ollama LLM initialization
│   ├── main.py                # Entry point for Ollama agent demo
│   └── tools_setup.py         # Tool definitions and setup
│
├── openai_agent/              # (Planned) OpenAI agent implementation
│   └── agent_demo.py          # Demo for OpenAI agent (future expansion)
│
├── venv/                      # Local virtual environment (not tracked by Git)
│
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
└── .gitignore                 # Ignore rules for Git
```

---

## Features

### Current

* **Ollama Agent Demo**

  * Connects to an Ollama model running locally (`localhost:11434`)
  * Uses `llm_setup.py` to initialize and run the model
  * Structured to allow adding tools and configuration easily

### Planned

* **OpenAI Agent Demo**

  * Similar architecture to Ollama agent
  * Will allow switching between LLM providers

* **FastAPI Backend**

  * Expose agent capabilities via REST API
  * Integrate with external applications (e.g., Android apps)

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd agenticAI-demo
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Ollama locally

Make sure Ollama is installed and running:

```bash
ollama serve
ollama run <model-name>
```

### 5. Run the Ollama agent

```bash
python ollama_agent/main.py
```

---

## Requirements

Dependencies are listed in `requirements.txt`. Example:

```txt
langchain
requests
python-dotenv
```

---

## Roadmap

* [x] Initial Ollama agent implementation
* [ ] Add OpenAI agent
* [ ] Build FastAPI backend for agents
* [ ] Integrate API with Android application

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.
