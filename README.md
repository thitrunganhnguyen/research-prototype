# 🔎 Research Assistant

AI-powered Research Assistant prototype for collecting information from web sources and generating structured research reports.

---

## Project Goal

The goal of this project is to explore how Large Language Models (LLMs) and web search can support research activities.

The application allows users to enter a research question and automatically:

- search relevant information from the web
- collect and summarize results
- generate a structured research report
- provide source references

This prototype focuses on usability, automation, and fast access to information.

---

## Features

### ⚡ Fast Research

Direct research workflow optimized for speed.

Process:

1. User enters research question
2. System performs web search
3. Results are collected
4. LLM generates final report
5. Sources are displayed

Best for:
- quick overview
- fast information gathering

---

### 🧠 Agent Research

Agent-based workflow.

Process:

1. Analyze research question
2. Plan search strategy
3. Execute multiple search steps
4. Collect information
5. Generate final synthesis

Best for:
- more complex topics
- deeper analysis

Note:
Agent mode may require more API requests than Fast Research.

---

## Output Format

After submitting a research question, the application generates a structured report.

Current output sections:

### Summary
Short overview of the topic.

### Key Findings
Most important insights extracted from sources.

### Advantages / Main Points
Structured explanation of important arguments.

### Risks / Limitations
Possible limitations or missing information.

### Conclusion
Final synthesized answer.

### Sources
List of sources used during research.

Example:

```text
Research Report

Summary
...

Key Findings
...

Advantages
...

Risks / Limitations
...

Conclusion
...

Sources
1. Source A
2. Source B
3. Source C
```

Additional features:

- Download report as Markdown
- Display source links
- Interactive UI

---

## Tech Stack

### Backend
- Python

### AI / LLM
- LangChain
- Google Gemini

### Search
- DuckDuckGo Search (ddgs)

### Frontend
- Streamlit

---

## Project Structure

```text
research-prototype/
│
├── app.py
├── web_app.py
├── requirements.txt
├── .env.sample
├── README.md
│
└── services/
    ├── __init__.py
    ├── llm_service.py
    ├── search_service.py
    ├── prompt_service.py
    ├── output_service.py
    └── agent_service.py
```

---

## Installation

Clone repository:

```bash
git clone git@github.com:thitrunganhnguyen/research-prototype.git
cd research-prototype
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

Linux / Mac:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Setup

Create environment file:

```bash
cp .env.sample .env
```

Add your Gemini API Key:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## Run Application

Start Web UI:

```bash
streamlit run web_app.py
```

Open browser:

```text
http://localhost:8501
```

---

## Example Questions

Business:

```text
What are the main advantages of SaaS ERP systems?
```

Technology:

```text
What are the latest AI trends in business applications?
```

Architecture:

```text
What are the principles of modern cloud architecture?
```

Politics:

```text
Analyze migration policy in Europe between 2015 and 2025.
```

