from pydantic import BaseModel

class RemoveBackgroundRequest(BaseModel):
    image_url: str