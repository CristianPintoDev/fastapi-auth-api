from passlib.context import CryptContext
from datetime import datetime, timezone, timedelta
from jose import jwt
from app.core.config import settings



pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode= data.copy()

    if expires_delta:
        expiree= datetime.now(timezone.utc) + expires_delta
    else:
        expiree= datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expiree})

    encode_jwt = jwt.encode(
        to_encode, 
        settings.SECRET_KEY, 
        algorithm=settings.ALGORITHM)

    return encode_jwt

    
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, password_hash: str) -> bool:
    return pwd_context.verify(password, password_hash)
