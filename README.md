# Email Composer AI

Email Composer AI is a simple, interactive web application that helps you generate high-quality emails based on a given purpose, tone, and content. It leverages Groq’s fast LLMs like LLaMA3 through LangChain and provides a streamlined interface using Streamlit.

---

## Features

- Compose emails for different purposes and tones (e.g., formal, friendly, thank-you).
- Uses Groq’s `llama3-70b-8192` model for fast, high-quality text generation.
- Built with LangChain to manage prompt templates and LLM chains.
- Interactive web-based UI using Streamlit.
- API keys are securely managed through environment variables.

---

## Technologies Used

| Tool/Library     | Purpose                          |
|------------------|----------------------------------|
| Python           | Core development language        |
| Streamlit        | Web-based frontend interface     |
| LangChain        | Prompt and LLM chain management  |
| Groq API         | LLM inference backend            |
| python-dotenv    | Load environment variables       |

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/email-composer-ai.git
cd email-composer-ai
