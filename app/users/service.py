from app.users.schema import UserCreate, UserResponse
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