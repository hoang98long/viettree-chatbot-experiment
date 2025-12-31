# app/integrations/n8n/webhook.py
from fastapi import APIRouter

router = APIRouter()

@router.post("/n8n/chat")
def n8n_chat(payload: dict):
    return {"answer": run_rag(payload["question"])}
