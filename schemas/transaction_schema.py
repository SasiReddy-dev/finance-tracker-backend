from pydantic import BaseModel
from datetime import date

class TransactionCreate(BaseModel):
    amount: float
    type: str
    category: str
    date: date
    notes: str

class TransactionUpdate(BaseModel):
    amount: float
    category: str
    notes: str