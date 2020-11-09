from datetime import datetime

from pydantic import BaseModel, Field


class Message(BaseModel):
    id: int = Field(..., ge=0)
    owner_id: int = Field(..., ge=0)
    timestamp: datetime
    content: str
