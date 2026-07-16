from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
key=os.getenv("api_key")
client = genai.Client(api_key=key)
 
response = client.models.generate_content(
    model="gemini-3.1-flash-lite-preview",
    contents="hi ai, who is cm of tamilnadu?"
)
 
print(response.text)
 