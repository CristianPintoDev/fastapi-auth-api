from fastapi import FastAPI
from app.users.router import router as user_router

app = FastAPI(title="FastAPI Backend Learning")

app.include_router(user_router)