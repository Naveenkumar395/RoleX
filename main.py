from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from rbac import require_role

# Create FastAPI app
app = FastAPI()

# Dummy function to simulate getting a user's role (in a real app, this would come from a user database or JWT token)
def get_user_role() -> str:
    return "admin"  # Change this to test different roles like "user", "moderator", etc.

class User(BaseModel):
    username: str
    email: str

# Get the role of the user and apply the role-based control
@app.get("/admin")
def get_admin(user_role: str = Depends(get_user_role)):
    require_role("admin", user_role)
    return {"message": "Welcome, Admin!"}


@app.get("/moderator")
def get_moderator(user_role: str = Depends(get_user_role)):
    require_role("moderator", user_role)  # Passing the user_role directly
    return {"message": "Welcome, Moderator!"}

@app.get("/user")
def get_user(user_role: str = Depends(get_user_role)):
    require_role("user", user_role)  # Passing the user_role directly
    return {"message": "Welcome, User!"}

@app.get("/")
def read_root():
    return {"message": "Welcome to the RBAC system!"}
