from groq import Groq
import os

client = Groq(api_key=os.getenv('Groq_API_Key'))

def create_description_with_ai(todo_title):
    completion = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[
        {
            "role": "system",
            "content": "You are helpful AI agent. Respond in json."
        },
        {
            "role": "user",
            "content": f"Give me a brief description for my todo : {todo_title}"
        }
        
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    return completion.choices[0].message.content

