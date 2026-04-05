from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import user_routes, transaction_routes, analytics_routes

app = FastAPI()

# ✅ CORS (keep this)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Home route
@app.get("/")
def home():
    return {"message": "Finance API Running 🚀"}

# ✅ Include routers
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(transaction_routes.router, prefix="/transactions", tags=["Transactions"])
app.include_router(analytics_routes.router, prefix="/analytics", tags=["Analytics"])
from database import Base, engine
from models import user, transaction


Base.metadata.create_all(bind=engine)

import os

port = int(os.environ.get("PORT", 10000))