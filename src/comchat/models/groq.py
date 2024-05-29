import os
from groq import Groq as GroqAI

class Groq:
    def __init__(self, model_name):
        self.model_name = model_name
        # Initialize Groq API client

    def generate(self, prompt):
        client = GroqAI(
            api_key=os.environ.get("GROQ_API_KEY"),
        )

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=self.model_name,
        )

        return chat_completion.choices[0].message.content