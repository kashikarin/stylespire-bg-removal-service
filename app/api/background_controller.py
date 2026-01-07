from fastapi import APIRouter, HTTPException
from fastapi.responses import Response

from app.models.requests import RemoveBackgroundRequest
from app.services.background_service import remove_background_from_url

router = APIRouter(prefix="/remove-background", tags=["background"])

@router.post("")

def remove_background(payload: RemoveBackgroundRequest):
    try:
        png_bytes = remove_background_from_url(payload.image_url)
        return Response(content=png_bytes, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

