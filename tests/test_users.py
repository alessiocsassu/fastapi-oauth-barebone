import pytest
import httpx
import random
from app.config.config import settings, Messages
from fastapi import status

random_username = "user" + str(random.randint(1000, 9999))

access_token = ""

def test_register_user():
    response = httpx.post(f"{settings.BASE_URL}/register", json={"username": random_username, "email": random_username + "@example.com", "password": "password"})
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["user"]["username"] == random_username

def test_login_user():
    response = httpx.post(f"{settings.BASE_URL}/login", data={"username": random_username, "password": "password"})
    assert response.status_code == status.HTTP_200_OK
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"
    global access_token 
    access_token = response.json()["access_token"]
    
def test_login_with_wrong_credentials():
    response = httpx.post(f"{settings.BASE_URL}/login", data={"username": random_username, "password": "wrongpassword"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json()["detail"] == Messages.INVALID_CREDENTIALS

#get users/me
def test_get_user_details():
    headers = {"Authorization": f"Bearer {access_token}"}
    response = httpx.get(f"{settings.BASE_URL}/users/me", headers=headers)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["username"] == random_username
    assert response.json()["email"] == random_username + "@example.com"

def test_update_user_details():
    headers = {"Authorization": f"Bearer {access_token}"}
    response = httpx.put(f"{settings.BASE_URL}/users/me", json={"username": random_username + "updated", "email": random_username + "@example.com"}, headers=headers)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["username"] == random_username + "updated"
    assert response.json()["email"] == random_username + "@example.com"

def test_get_updated_user_details():
    headers = {"Authorization": f"Bearer {access_token}"}
    response = httpx.get(f"{settings.BASE_URL}/users/me", headers=headers)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["username"] == random_username + "updated"
    assert response.json()["email"] == random_username + "@example.com"

def test_delete_user():
    headers = {"Authorization": f"Bearer {access_token}"}
    response = httpx.delete(f"{settings.BASE_URL}/users/me", headers=headers)
    assert response.status_code == status.HTTP_204_NO_CONTENT