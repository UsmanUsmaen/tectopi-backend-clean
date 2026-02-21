from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="TECTOPI Backend")

# -------- Models --------
class ChatRequest(BaseModel):
    message: str

# -------- Routes --------
@app.get("/")
def root():
    return {"message": "TECTOPI backend running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ai/chat")
def chat(req: ChatRequest):
    # Temporary response (we plug real AI next)
    return {
        "response": f"TECTOPI AI received: {req.message}",
        "mode": "mock"
    }
