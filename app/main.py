from fastapi import FastAPI
from app.users.router import router as user_router
from app.core.database import engine, Base
from app.users import model



app = FastAPI(title="FastAPI Backend Learning")

app.include_router(user_router)

Base.metadata.create_all(bind=engine)