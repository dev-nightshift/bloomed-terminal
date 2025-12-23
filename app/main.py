from fastapi import FastAPI

from app.core.cors import add_cors
from app.api.routes import api_router

app = FastAPI(title="Claude Companions Backend", version="0.1.0")

add_cors(app)
app.include_router(api_router)


@app.get("/health")
def health():
    return {"ok": True}
