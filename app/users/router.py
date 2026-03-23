from fastapi import APIRouter, HTTPException, Path, Depends
from app.auth.dependencies import get_current_user
from app.users.model import User
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.users.schema import UserCreate, UserResponse, UserUpdate
from app.users.service import create_user, list_users, get_user, update_user, delete_user


router= APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", response_model=UserResponse)
def create_user_endpoint(
    user: UserCreate,
    db: Session = Depends(get_db)):
    return create_user(db, user)


@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return list_users(db)

@router.get("/me")
def read_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(
    user_id: str,
    db: Session = Depends(get_db)
    ):
    user =get_user(db, user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
            )
    return user

@router.put("/{user_id}", response_model=UserResponse)
def update_user_endpoint(user_id: str, 
                         user_data: UserUpdate,
                         db: Session = Depends(get_db)
                         ):
    user = update_user(db, user_id, user_data)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user
    
@router.delete("/{user_id}", response_model=UserResponse)
def delete_user_endpoint(
    user_id: str,
    db: Session = Depends(get_db)
    ):
    user = delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user
    
