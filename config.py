import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get("SESSION_SECRET", "dev-secret-key")
    SPOONACULAR_API_KEY = os.environ.get("SPOONACULAR_API_KEY", "")
    OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
    OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
