from sqlalchemy.orm import Session
from app.users.model import User
from datetime import timedelta
from app.core.security import verify_password, create_access_token
from app.core.config import settings

def login_user(db, email: str, password: str):
    user= db.query(User).filter(User.email == email).first()
    if not user:
        return None
    
    if not verify_password(password, user.password_hash):
        return None
    

    access_token= create_access_token(
        data={"sub": user.id},
        expires_delta=timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
            )
    )
    
    return access_token