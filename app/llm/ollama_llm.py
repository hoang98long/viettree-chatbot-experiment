# app/llm/ollama_llm.py
import requests
from .base import BaseLLM

class OllamaLLM(BaseLLM):
    def __init__(self, model="llama3"):
        self.url = "http://localhost:11434/api/chat"
        self.model = model

    def chat(self, messages, **kwargs):
        r = requests.post(self.url, json={
            "model": self.model,
            "messages": messages,
            "stream": False
        })
        return r.json()["message"]["content"]
