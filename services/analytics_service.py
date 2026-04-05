from models.transaction import Transaction
from sqlalchemy.orm import Session
from sqlalchemy import func

def get_summary(db: Session, user_id: int):
    total_income = db.query(func.sum(Transaction.amount)).filter(
        Transaction.user_id == user_id,
        Transaction.type == "income"
    ).scalar() or 0

    total_expense = db.query(func.sum(Transaction.amount)).filter(
        Transaction.user_id == user_id,
        Transaction.type == "expense"
    ).scalar() or 0

    balance = total_income - total_expense

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance
    }
def category_summary(db: Session, user_id: int):
    result = db.query(
        Transaction.category,
        func.sum(Transaction.amount)
    ).filter(
        Transaction.user_id == user_id
    ).group_by(Transaction.category).all()

    return [{"category": r[0], "total": r[1]} for r in result]
from sqlalchemy import extract

def monthly_summary(db: Session, user_id: int):
    result = db.query(
        extract('month', Transaction.date).label("month"),
        func.sum(Transaction.amount)
    ).filter(
        Transaction.user_id == user_id
    ).group_by("month").all()

    return [{"month": int(r[0]), "total": r[1]} for r in result]
def recent_transactions(db: Session, user_id: int):
    return db.query(Transaction).filter(
        Transaction.user_id == user_id
    ).order_by(Transaction.date.desc()).limit(5).all()