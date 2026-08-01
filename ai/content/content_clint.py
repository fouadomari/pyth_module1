import os
from openai import OpenAI
from decouple import config

print(config("OPENAI_API_KEY"))
class ContentClient:
    def __init__(self):
        # Read the API key from env (do not hardcode it)
        api_key = config("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key)
        
        # Use a small, cheap chat model suitable for summaries
        self.model = "gpt-4o-mini"

    def generate(self, prompt: str) -> str:
        """Sends the prompt to OpenAI and returns the reply as plain text."""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        # Return model's reply as plain text (a string)
        return response.choices[0].message.content