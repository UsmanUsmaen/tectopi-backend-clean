from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI(title="TECTOPI Backend")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "TECTOPI backend running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ai/chat")
def chat(req: ChatRequest):

    completion = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are TECTOPI AI. You help with education, finance and sustainability guidance for African communities."},
            {"role": "user", "content": req.message}
        ]
    )

    return {
        "response": completion.choices[0].message.content,
        "mode": "real-ai"
    }
