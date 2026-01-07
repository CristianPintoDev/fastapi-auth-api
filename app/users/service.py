from app.users.schema import UserCreate, UserResponse, UserUpdate
from uuid import uuid4


_fake_users_db = []

def create_user(user: UserCreate) -> UserResponse:
    new_user = UserResponse(
        id=str(uuid4()),
        email=user.email,
        name=user.name,
        is_active=True
    )
    _fake_users_db.append(new_user)
    return new_user



def list_users():
    return _fake_users_db

def get_user(user_id: str) -> UserResponse | None:
    for user in _fake_users_db:
        if user.id == user_id:
            return user
    return None

def update_user(user_id: str, user_data: UserUpdate):
    user= get_user(user_id)
    if not user:
        return None
    
    if user_data.email is not None:
        user.email= user_data.email
    
    if user_data.name is not None:
        user.name= user_data.name
    
    if user_data.is_active is not None:
        user.is_active= user_data.is_active

    return user

def delete_user(user_id: str):
    global _fake_users_db
    user=get_user(user_id)
    if not user:
        return None
    
    _fake_users_db= [u for u in _fake_users_db if u.id !=user_id]
    return user