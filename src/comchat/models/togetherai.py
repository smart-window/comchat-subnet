import os
from together import Together

class TogetherAI:
    def __init__(self, model_name):
        self.model_name = model_name
        # Initialize TogetherAI API client

    def generate(self, prompt):

        client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

        response = client.chat.completions.create(
            model=self.model_name,
            messages=[
                {
                    "role": "user", 
                    "content": prompt
                    }
                ],
        )
        return response.choices[0].message.content
    