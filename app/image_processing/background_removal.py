from rembg import remove
from PIL import Image

def remove_background(image: Image.Image) -> Image.Image:
    try:
        if image.mode != "RGBA":
            image = image.convert("RGBA")
        return remove(image)
    except Exception:
        raise RuntimeError("Background removal failed")

