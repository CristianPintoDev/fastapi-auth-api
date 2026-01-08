from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    name: str
    password: str

    @field_validator("password")
    @classmethod
    def validate_password_length(cls, value: str):
        if len(value.encode("utf-8")) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")
        return value




class UserResponse(BaseModel):
    id: str
    email: EmailStr
    name: str
    is_active: bool

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str]= None
    password: Optional[str]= None
    is_active: bool | None= None

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str | None) -> str | None:
        if value is not None and len(value) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")
        return value


class UserLogin(BaseModel):
    email: EmailStr
    password: str


