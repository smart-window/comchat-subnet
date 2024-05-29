import os
import openai

class OpenAI:
    def __init__(self, model_name):
        self.model_name = model_name
        openai.api_key = os.environ["OPENAI_API_KEY"]

    def generate(self, prompt):
        from openai import OpenAI
        client = OpenAI()

        completion = client.chat.completions.create(
        model=self.model_name,
        messages=[
            {"role": "user", "content": prompt}
        ]
        )

        return completion.choices[0].message.content
