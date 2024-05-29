import os
import google.generativeai as genai

class Gemini:
    def __init__(self, model_name):
        self.model_name = model_name
        try:
            # Initialize Gemini API client
            self.model = genai.GenerativeModel(self.model_name)
            genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
        except Exception as e:
            print(f"Unexpected error during initialization: {e}")
            self.model = None

    def generate(self, prompt):
        if not self.model:
            return "Model is not initialized due to previous errors."

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Unexpected error during content generation: {e}")
            return "An unexpected error occurred during content generation."
