from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.user_schema import UserCreate, UserLogin
from services.user_service import create_user, authenticate_user
from auth.jwt_handler import create_token

router = APIRouter()

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.email, user.password)
    
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_token({"user_id": db_user.id, "role": db_user.role})
    
    return {"access_token": token}