#for ORM
from sqlmodel import SQLModel, create_engine, Session
# for .env handling
from dotenv import load_dotenv
import os
# for easier way for session dependency
from typing import Annotated
from fastapi import Depends



load_dotenv()
DATABASE_URL=os.getenv("DATABASE_URL") # getting credentials from .env instead of hardcoding
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL not found in .env file")
engine = create_engine(DATABASE_URL,echo=True)

def create_db_and_tables():
    # creating all table using SQLModel
    SQLModel.metadata.create_all(engine)

def get_session():
    # "database session per request only" dependency
    with Session(engine) as session:
        yield session

Session_Depends = Annotated[Session, Depends(get_session)]