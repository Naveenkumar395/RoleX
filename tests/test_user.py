from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_user():
    response = client.post("/users/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123",
        "role": "User"
    })
    assert response.status_code == 201
    assert response.json()["username"] == "testuser"

def test_login_user():
    response = client.post("/users/login", json={
        "username": "testuser",
        "password": "password123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_admin_access():
    # Replace with token retrieval logic
    token = "dummy-admin-token"
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/admin/dashboard", headers=headers)
    assert response.status_code == 200
    assert "message" in response.json()
