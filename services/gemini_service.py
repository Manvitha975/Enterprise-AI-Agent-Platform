import os
from pathlib import Path

from dotenv import load_dotenv
import google.generativeai as genai

# Absolute path to the .env file
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

print("Looking for .env at:", ENV_FILE)
print(".env exists:", ENV_FILE.exists())

load_dotenv(dotenv_path=ENV_FILE)

api_key = os.getenv("GEMINI_API_KEY")

print("Loaded API Key:", api_key[:10] + "..." if api_key else "NOT FOUND")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_gemini(question: str):
    response = model.generate_content(question)
    return response.text