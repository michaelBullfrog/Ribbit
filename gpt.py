# gpt.py
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

def ask_chatgpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a product quoting assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
