from pydantic import BaseModel

class StandardResponse(BaseModel):
    message: str