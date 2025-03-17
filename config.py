import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_GENAI_API_KEY=os.getenv("GOOGLE_GENAI_API_KEY")

if not GOOGLE_GENAI_API_KEY:
    raise ValueError("Google GenAI API key is missing!")


MODEL_NAME = "models/gemini-1.5-pro"