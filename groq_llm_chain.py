from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from prompt import get_email_prompt
from dotenv import load_dotenv
import os

load_dotenv()  # ✅ Make sure to load environment variables

# Set the Groq endpoint for LangChain to use ChatOpenAI interface
os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"

def generate_email(purpose, tone, details):
    llm = ChatOpenAI(
        model_name="llama3-70b-8192",
        temperature=0.7,
        openai_api_key=os.getenv("GORQ_API")  # ✅ Must be this key name
    )

    prompt = get_email_prompt()  # ✅ Function call

    chain = LLMChain(llm=llm, prompt=prompt)

    return chain.run({
        "purpose": purpose,
        "tone": tone,
        "details": details
    })
