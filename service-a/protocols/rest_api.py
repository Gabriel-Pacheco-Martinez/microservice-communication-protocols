from fastapi import FastAPI, APIRouter, Depends, HTTPException
from models import User
from database import SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List
from schemas import UserOut, UserCreate

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
@app.on_event("startup")
def startup_event():
    print("✅ Service A is up and running on http://0.0.0.0:8000")

@router.get("/users", response_model=List[UserOut])
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.post("/users", response_model=List[UserOut])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check for required fields
    if not user.name or not user.email:
        raise HTTPException(status_code=400, detail="Missing name or email")

    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return db.query(User).all()    

@app.get("/ping")
def ping(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1")).scalar()
    return {"db_connection": "ok" if result == 1 else "fail"}

# ====
# Add endpoint to router
app.include_router(router)
