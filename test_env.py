from pathlib import Path
from dotenv import load_dotenv
import os

print("Current directory:", Path.cwd())

env_path = Path(".env")
print(".env exists:", env_path.exists())

load_dotenv(dotenv_path=env_path)

print("API Key:", os.getenv("GEMINI_API_KEY"))