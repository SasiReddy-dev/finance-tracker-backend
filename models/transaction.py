from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Date, Float
from database import Base
import enum

class TransactionType(str, enum.Enum):
    income = "income"
    expense = "expense"

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float)
    type = Column(Enum(TransactionType))
    category = Column(String(100))
    date = Column(Date)
    notes = Column(String(255))