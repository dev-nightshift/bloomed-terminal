from fastapi import APIRouter, HTTPException

from app.domain.companions import CompanionId
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.anthropic_client import ask_claude

router = APIRouter()


@router.post("/{companion_id}", response_model=ChatResponse)
def chat(companion_id: CompanionId, payload: ChatRequest):
    try:
        text, model = ask_claude(companion_id, payload.messages)
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Claude request failed: {e}")

    return ChatResponse(companion_id=companion_id, model=model, text=text)
