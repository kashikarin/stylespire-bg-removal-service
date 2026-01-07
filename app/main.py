from fastapi import FastAPI
from app.api.background_controller import router as background_router

app = FastAPI(title="Background Removal Service")

app.include_router(background_router)

@app.get("/health")
def health():
    return {"status": "ok"}

