from fastapi import APIRouter, HTTPException, Path
from app.users.schema import UserCreate, UserResponse, UserUpdate
from app.users.service import create_user, list_users, get_user, update_user, delete_user


router= APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", response_model=UserResponse)
def create_user_endpoint(user: UserCreate):
    return create_user(user)


@router.get("/", response_model=list[UserResponse])
def get_users():
    return list_users()

@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(
    user_id: str = Path(..., description="ID del usuario")
    ):
    user =get_user(user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
            )
    return user

@router.put("/{user_id}", response_model=UserResponse)
def update_user_endpoint(user_id: str, user_data: UserUpdate):
    user = update_user(user_id, user_data)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user
    
@router.delete("/{user_id}", response_model=UserResponse)
def delete_user_endpoint(user_id: str):
    user = delete_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user
    
