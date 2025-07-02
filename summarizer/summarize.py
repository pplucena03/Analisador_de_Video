import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def summarize_text(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"Resuma o seguinte texto no seu respectivo idioma:\n\n{text}"
            }
        ],
    temperature=0.3
)
    return response.choices[0].message.content