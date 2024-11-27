from fastapi import APIRouter, Depends
from auth import create_access_token, verify_password, get_password_hash
from models import User
from database import SessionLocal

router = APIRouter()

@router.post("/register")
def register_user(username: str, password: str):
    db = SessionLocal()
    hashed_password = get_password_hash(password)
    new_user = User(username=username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.close()
    return {"message": "User registered successfully"}

@router.post("/login")
def login_user(username: str, password: str):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": username, "role": user.role})
    return {"access_token": token, "token_type": "bearer"}
