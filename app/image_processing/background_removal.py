
from rembg import remove, new_session
from PIL import Image
from io import BytesIO

session = new_session("u2netp")

def remove_background(image: Image.Image) -> Image.Image:
    try:
        if image.mode != "RGBA":
            image = image.convert("RGBA")

            input_buffer = BytesIO()
            image.save(input_buffer, format="PNG")

            output_bytes = remove(input_buffer.getvalue(), session=session)

            return Image.open(BytesIO(output_bytes)).convert("RGBA")
        
        return remove(image)
    except Exception as e:
        raise RuntimeError(f"Background removal failed: {e}")

