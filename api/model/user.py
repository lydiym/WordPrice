from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    id: int = Field(..., ge=0)
    name: str = Field(..., max_length=100)
    email: EmailStr
    bch_address: str = Field(..., max_length=100)
