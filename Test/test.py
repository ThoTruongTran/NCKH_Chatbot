import google.generativeai as genai
print("OK, version:", getattr(genai, "__version__", "unknown"))

import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)
