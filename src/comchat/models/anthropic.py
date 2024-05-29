import anthropic
import os

class Anthropic:
    def __init__(self, model_name):
        self.model_name = model_name
        # Initialize Anthropic API client

    def generate(self, prompt):

        client = anthropic.Anthropic(
            api_key=os.environ.get("ANTHROPIC_API_KEY"),
        )

        message = client.messages.create(
            max_tokens=1024,
            model=self.model_name,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        result = "".join(block['text'] for block in message.model_dump()['content'] if block['type'] == 'text')

        return result