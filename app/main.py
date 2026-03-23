from fastapi import FastAPI
from app.users.router import router as user_router
from app.auth.router import router as auth_router
from app.core.database import engine, Base
from app.users import model



app = FastAPI(title="FastAPI auth API")

app.include_router(user_router)
app.include_router(auth_router)



Base.metadata.create_all(bind=engine)