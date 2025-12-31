# app/llm/gpt_oss_llm.py
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class GPTOSSLLM:
    def __init__(self, model_id):
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id, torch_dtype=torch.float16
        ).cuda()

    def chat(self, prompt: str):
        inputs = self.tokenizer(prompt, return_tensors="pt").to("cuda")
        out = self.model.generate(**inputs, max_new_tokens=512)
        return self.tokenizer.decode(out[0], skip_special_tokens=True)
