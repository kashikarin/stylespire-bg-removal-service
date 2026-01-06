from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
import requests
from rembg import remove
from PIL import Image
from io import BytesIO

app = FastAPI(title="Background Removal Service")

class RemoveBackgroundRequest(BaseModel):
    image_url: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/remove-background")
def remove_background(payload: RemoveBackgroundRequest):
    image_url = payload.image_url

# Fetch the image from the provided URL
    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Error fetching image: {e}")   

# Load the image
    try:
        input_image = Image.open(BytesIO(response.content)).convert("RGBA")
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid image format")
    
# Remove the background
    try:
        output_image = remove(input_image)
    except Exception:
        raise HTTPException(status_code=500, detail="Background removal failed")
    
# Convert output image to PNG bytes
    output_buffer = BytesIO()
    output_image.save(output_buffer, format="PNG")
    png_bytes = output_buffer.getvalue()

# Return the processed image
    return Response(content=png_bytes, media_type="image/png")        
     