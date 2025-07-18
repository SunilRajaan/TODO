from groq import Groq
import os

client = Groq(api_key=os.getenv('Groq_API_Key'))

def create_description_with_ai(todo_title):
    completion = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[
        {
            "role": "system",
            "content": "you are descriptionist for todo. Respond in json format with only"
        },
        {
            "role": "user",
            "content": f"give me a breif description according for todo title : {todo_title}"
        }
        ],
        temperature=1,
        max_completion_tokens=300,
        top_p=1,
        stream=False,
        response_format={"type": "json_object"},
        stop=None,
    )

    return completion.choices[0].message.content


