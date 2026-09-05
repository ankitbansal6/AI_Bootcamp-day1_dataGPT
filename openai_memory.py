from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

chat_history =[] 

while True :
    user_input = input("ask your question: ")
    chat_history.append(user_input)
    response  = client.responses.create(model='gpt-5.6-sol',
                                    input = chat_history)
    chat_history.append(response.output_text)
    print(response.output_text)

