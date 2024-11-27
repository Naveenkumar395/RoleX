from fastapi import HTTPException, status

# Sample user roles
ROLES = ["admin", "moderator", "user"]

# Function to check if the user has the required role
def require_role(required_role: str, user_role: str):
    """
    Enforce role-based access control by checking if the user's role
    matches the required role.
    
    Args:
        required_role (str): The role required to access the resource.
        user_role (str): The role of the current user.

    Raises:
        HTTPException: If the user does not have the required role.
    """
    if user_role != required_role:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Access denied. User must have the '{required_role}' role."
        )


# Additional helper functions (optional)
def is_admin(user_role: str) -> bool:
    return user_role == "admin"

def is_moderator(user_role: str) -> bool:
    return user_role == "moderator"
