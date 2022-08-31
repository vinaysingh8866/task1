import json
import pytest
from app import app
client = app.test_client()
def test_register():
    response = client.post(
        "/api/register", json={
            "email": "vinaysingh8866@gmail.com",
            "upassword": "123456789",
            "uname": "vinaysingh"})
    assert response.status_code == 200

def test_login():
    response = client.post(
        "/api/login", json={
            "email": "vinaysingh8866@gmail.com",
            "upassword": "123456789"})
    print(response.json)
    assert response.status_code == 200

test_register()
test_login()