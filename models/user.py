from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP
from database import Base
import enum
from datetime import datetime

class UserRole(str, enum.Enum):
    admin = "admin"
    analyst = "analyst"
    viewer = "viewer"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    password = Column(String(255))
    role = Column(Enum(UserRole), default=UserRole.viewer)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)