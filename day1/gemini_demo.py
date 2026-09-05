from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

response = client.models.generate_content(
            model= 'gemini-3.5-flash',
            contents= "tell me about apache spark in 10 words")

print(response.text)

