from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from auth.dependencies import get_current_user
from services.analytics_service import *

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/summary")
def summary(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return get_summary(db, user.id)


@router.get("/category")
def category(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return category_summary(db, user.id)


@router.get("/monthly")
def monthly(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return monthly_summary(db, user.id)


@router.get("/recent")
def recent(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return recent_transactions(db, user.id)