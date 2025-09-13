import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

img = Image.open(r"D:\NCKH_TTT\Test\test_image.jpg")

response = model.generate_content(
    [img, "Mô tả chi tiết bức ảnh này."]
)

print(response.text)
