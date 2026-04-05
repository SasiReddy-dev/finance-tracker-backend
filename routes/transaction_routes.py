from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.transaction_schema import TransactionCreate, TransactionUpdate
from services.transaction_service import (
    create_transaction,
    get_transactions_filtered,
    update_transaction,
    delete_transaction,
    get_transactions_paginated
)
from auth.dependencies import get_current_user, require_admin

router = APIRouter()

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🔹 CREATE (Admin only)
@router.post("/")
def create_txn(
    data: TransactionCreate,
    db: Session = Depends(get_db),
    user = Depends(require_admin)
):
    return create_transaction(db, user.id, data)


# 🔹 GET (with FILTERING)
@router.get("/")
def get_txns(
    type: str = None,
    category: str = None,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return get_transactions_filtered(db, user.id, type, category)


# 🔹 UPDATE (Admin only)
@router.put("/{txn_id}")
def update_txn(
    txn_id: int,
    data: TransactionUpdate,
    db: Session = Depends(get_db),
    user = Depends(require_admin)
):
    txn = update_transaction(db, txn_id, data)

    if not txn:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return txn


# 🔹 DELETE (Admin only)
@router.delete("/{txn_id}")
def delete_txn(
    txn_id: int,
    db: Session = Depends(get_db),
    user = Depends(require_admin)
):
    txn = delete_transaction(db, txn_id)

    if not txn:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return {"message": "Deleted successfully"}


# 🔹 PAGINATION
@router.get("/paginated")
def get_txns_paginated(
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    skip = (page - 1) * limit
    return get_transactions_paginated(db, user.id, skip, limit)