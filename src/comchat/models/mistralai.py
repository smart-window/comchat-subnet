from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import os

class MistralAI:
    def __init__(self, model_name):
        self.model_name = model_name
        # Initialize MistralAI API client

    def generate(self, prompt):

        api_key = os.environ["MISTRAL_API_KEY"]
        model = self.model_name

        client = MistralClient(api_key=api_key)

        messages = [
            ChatMessage(role="user", content=prompt)
        ]

        # No streaming
        chat_response = client.chat(
            model=model,
            messages=messages,
        )

        return chat_response.choices[0].message.content