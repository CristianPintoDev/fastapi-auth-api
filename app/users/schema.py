from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    name: str

class UserResponse(BaseModel):
    id: str
    email: EmailStr
    name: str
    is_active: bool