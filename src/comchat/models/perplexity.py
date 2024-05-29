from openai import OpenAI
import os

class Perplexity:
    def __init__(self, model_name):
        self.model_name = model_name
        # Initialize Perplexity API client

    def generate(self, prompt):

        api_key = os.environ["PERPLEXITY_API_KEY"]

        messages = [
            {
                "role": "user",
                "content": (
                    prompt
                ),
            },
        ]

        client = OpenAI(api_key=api_key, base_url="https://api.perplexity.ai")

        # chat completion without streaming
        response = client.chat.completions.create(
            model=self.model_name,
            messages=messages,
        )
        
        return response.model_dump()["choices"][0]["message"]["content"]