import requests
import json
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

url = "https://api.openai.com/v1/engines/davinci-codex/completions"
headers = {
"Content-Type": "application/json",
"Authorization": f"Bearer {OPENAI_API_KEY}"
}
data = {
"prompt": "Translate the following English text to French: 'Hello, how are you?'",
"max_tokens": 60
}

response = requests.post(url, json=data, headers=headers)
completion = response.json()["choices"][0]["text"]
print("Completion:", completion)