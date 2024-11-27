from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from rbac import require_role
from models import User

router = APIRouter()

@router.get("/dashboard", dependencies=[Depends(require_role("Admin"))])
def admin_dashboard(db: Session = Depends(get_db)):
    # Example logic: Fetch all users
    users = db.query(User).all()
    return {"message": "Welcome to the Admin Dashboard", "users": users}

@router.delete("/delete-user/{user_id}", dependencies=[Depends(require_role("Admin"))])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
