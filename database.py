from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Get DB URL from .env
DATABASE_URL = os.getenv("DATABASE_URL")

# If not set → use SQLite (for deployment)
if not DATABASE_URL:
    DATABASE_URL = "sqlite:///./test.db"

# SQLite specific setting
connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

# Create engine
engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args
)

# Session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base
Base = declarative_base()