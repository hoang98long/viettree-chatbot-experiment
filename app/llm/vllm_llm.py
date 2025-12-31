# app/llm/vllm_llm.py
from openai import OpenAI
from .base import BaseLLM

class VLLMLLM(BaseLLM):
    def __init__(self):
        self.client = OpenAI(
            base_url="http://localhost:8000/v1",
            api_key="EMPTY"
        )

    def chat(self, messages, **kwargs):
        res = self.client.chat.completions.create(
            model="local-model",
            messages=messages,
        )
        return res.choices[0].message.content
