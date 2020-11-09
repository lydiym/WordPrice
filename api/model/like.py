from pydantic import BaseModel, Field

class User(BaseModel):
    owner_id: int = Field(..., ge=0)
    message_id: int = Field(..., ge=0)