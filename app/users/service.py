from app.users.schema import UserCreate, UserUpdate
from sqlalchemy.orm import Session
from app.users.model import User
from app.core.security import hash_password, verify_password



def create_user(db: Session, user: UserCreate):
    db_user = User(
        email=user.email,
        name=user.name,
        password_hash=hash_password(user.password),
        is_active=True
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    return user
    

def list_users(db: Session):
    return db.query(User).all()


def get_user(db: Session,user_id: str):
    return db.query(User).filter(User.id == user_id).first()


def update_user(db: Session, user_id: str, user_data: UserUpdate):
    user= get_user(db, user_id)
    if not user:
        return None
    
    if user_data.email is not None:
        user.email= user_data.email
    
    if user_data.name is not None:
        user.name= user_data.name
    
    if user_data.is_active is not None:
        user.is_active= user_data.is_active
    
    if user_data.password is not None:
        user.password_hash = hash_password(user_data.password)

    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: str):
    user=get_user(db, user_id)
    if not user:
        return None
    
    db.delete(user)
    db.commit()
    return user