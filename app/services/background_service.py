import requests
from PIL import Image
from io import BytesIO

from app.image_processing.background_removal import remove_background
from app.image_processing.subject_selection import select_largest_subject

def remove_background_from_url(image_url: str) -> bytes:
    image = _download_image(image_url)
    no_bg_image = remove_background(image)
    primary_subject_image = select_largest_subject(no_bg_image)
    return _image_to_png_bytes(primary_subject_image)

# helper functions

def _download_image(image_url: str) -> Image.Image:
    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Error fetching image: {e}")
    
    try:
        return Image.open(BytesIO(response.content)).convert("RGBA")
    except Exception:
        raise ValueError("Invalid image format")


def _image_to_png_bytes(image: Image.Image) -> bytes:
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return buffer.getvalue()

