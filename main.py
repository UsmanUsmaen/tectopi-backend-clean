from fastapi import FastAPI

app = FastAPI(title="TECTOPI Backend")

@app.get("/")
def root():
    return {"message": "TECTOPI backend running"}

@app.get("/health")
def health():
    return {"status": "ok"}