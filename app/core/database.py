from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session
from typing import Generator

DATABASE_URL= "sqlite:///./app.db"

engine = create_engine(
    DATABASE_URL, 
    echo=True
)

class Base(DeclarativeBase):
    pass

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()