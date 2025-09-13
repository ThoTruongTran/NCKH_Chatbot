import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

# Test model
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Xin chào, hãy giúp tôi viết một đoạn văn về trí tuệ nhân tạo.")
print(response.text)
