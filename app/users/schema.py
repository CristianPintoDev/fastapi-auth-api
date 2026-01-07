from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    name: str


class UserUpdate(BaseModel):
    email: EmailStr | None= None
    name: str | None= None
    is_active: bool | None= None


class UserResponse(BaseModel):
    id: str
    email: EmailStr
    name: str
    is_active: bool

