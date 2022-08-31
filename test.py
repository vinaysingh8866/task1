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
    assert response.status_code == 200

def add_tweet():
    login = client.post(
        "/api/login", json={
            "email": "vinaysingh8866@gmail.com",
            "upassword": "123456789"})
    token = login.json['token']
    response = client.post(
        "/api/add_tweet",headers={"Authorization": "Bearer " + token}, json={
            "title": "vinaysingh8866@gmail.com",
            "content": "123456789"})
    print(response.json)
    assert response.status_code == 200

def userTweets():
    login = client.post(
        "/api/login", json={
            "email": "vinaysingh8866@gmail.com",
            "upassword": "123456789"})
    token = login.json['token']
    response = client.post(
        "/api/user_tweets",headers={"Authorization": "Bearer " + token}, json={
            "uid": 1})
    print(response.json)

def update_tweet():
    login = client.post(
        "/api/login", json={
            "email": "vinaysingh8866@gmail.com",
            "upassword": "123456789"})
    token = login.json['token']
    response = client.post(
        "/api/update_tweet/1",headers={"Authorization": "Bearer " + token}, json={
            "content": "123jhbljb456789kjhfkjhf"})
    print(response.json)
    assert response.status_code == 200

test_register()
test_login()
add_tweet()
update_tweet()
userTweets()
