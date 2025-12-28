from fastapi import FastAPI

app = FastAPI(title="Market Data API")

@app.get("/")
def health_check():
    return {"status": "ok"}

