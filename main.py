from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI(title="TECTOPI Backend")

client = OpenAI()   # API key auto-read from environment

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
    try:
        completion = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are TECTOPI AI helping with education and financial inclusion in Africa."},
                {"role": "user", "content": req.message}
            ]
        )

        return {
            "response": completion.choices[0].message.content,
            "mode": "real-ai"
        }

    except Exception as e:
        # This prints the real error into Railway logs
        print("AI ERROR:", str(e))
        return {
            "error": "AI request failed",
            "details": str(e)
        }
