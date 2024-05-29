import requests
import json
import os

class OpenRouter:
    def __init__(self, model_name):
        self.model_name = model_name
        self.api_key = os.environ.get("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError("API key for OpenRouter is not set in environment variables.")

    def generate(self, prompt):
        if not prompt:
            raise ValueError("Prompt cannot be empty.")

        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                data=json.dumps({
                    "model": self.model_name,
                    "messages": [
                        {"role": "user", "content": prompt}
                    ]
                })
            )
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
            
            response_data = response.json()
            if 'choices' not in response_data or not response_data['choices']:
                raise ValueError("Invalid response format: 'choices' field is missing or empty.")
            
            return response_data['choices'][0]['message']['content']

        except requests.exceptions.RequestException as e:
            # Handle network-related errors
            print(f"Network error: {e}")
            raise

        except json.JSONDecodeError:
            # Handle JSON decoding errors
            print("Error decoding the response JSON.")
            raise

        except KeyError:
            # Handle missing keys in the response
            print("Unexpected response format.")
            raise

        except Exception as e:
            # Catch-all for any other exceptions
            print(f"An error occurred: {e}")
            raise