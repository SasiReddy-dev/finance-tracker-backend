from models.transaction import Transaction
from sqlalchemy.orm import Session


# 🔹 CREATE TRANSACTION
def create_transaction(db: Session, user_id: int, data):
    new_txn = Transaction(
        user_id=user_id,
        amount=data.amount,
        type=data.type,
        category=data.category,
        date=data.date,
        notes=data.notes
    )

    db.add(new_txn)
    db.commit()
    db.refresh(new_txn)

    return new_txn


# 🔹 GET ALL TRANSACTIONS (basic)
def get_transactions(db: Session, user_id: int):
    return db.query(Transaction)\
        .filter(Transaction.user_id == user_id)\
        .all()


# 🔹 UPDATE TRANSACTION (safe update)
def update_transaction(db: Session, txn_id: int, data):
    txn = db.query(Transaction).filter(Transaction.id == txn_id).first()

    if not txn:
        return None

    # update only if value provided
    if data.amount is not None:
        txn.amount = data.amount

    if data.category is not None:
        txn.category = data.category

    if data.notes is not None:
        txn.notes = data.notes

    if data.type is not None:
        txn.type = data.type

    if data.date is not None:
        txn.date = data.date

    db.commit()
    db.refresh(txn)

    return txn


# 🔹 DELETE TRANSACTION
def delete_transaction(db: Session, txn_id: int):
    txn = db.query(Transaction).filter(Transaction.id == txn_id).first()

    if not txn:
        return None

    db.delete(txn)
    db.commit()

    return txn


# 🔹 FILTERING (🔥 IMPORTANT)
def get_transactions_filtered(db: Session, user_id: int, type=None, category=None):
    query = db.query(Transaction).filter(Transaction.user_id == user_id)

    if type:
        query = query.filter(Transaction.type == type)

    if category:
        query = query.filter(Transaction.category == category)

    return query.all()


# 🔹 PAGINATION (🔥 IMPORTANT)
def get_transactions_paginated(db: Session, user_id: int, skip=0, limit=10):
    return db.query(Transaction)\
        .filter(Transaction.user_id == user_id)\
        .offset(skip)\
        .limit(limit)\
        .all()