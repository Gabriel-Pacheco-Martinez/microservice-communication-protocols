from fastapi import FastAPI, APIRouter, Depends
from models import User
from database import SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List
from schemas import UserOut

app = FastAPI()
router = APIRouter()

# ====
# Connect to db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ====
# Connections
@router.get("/users", response_model=List[UserOut])
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.get("/ping")
def ping(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1")).scalar()
    return {"db_connection": "ok" if result == 1 else "fail"}

# ====
# Add endpoint to router
app.include_router(router)
