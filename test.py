import json
import pytest
from app import app
client = app.test_client()


def testRegister():
    response = client.post(
        "/api/register", json={
            "email": "vinaysingh8866@gmail.com",
            "upassword": "123456789",
            "uname": "vinaysingh"})
    assert response.status_code == 200
    print("Testing Passed")


def testLogin():
    response = client.post(
        "/api/login", json={
            "email": "vinaysingh8866@gmail.com",
            "upassword": "123456789"})
    assert response.status_code == 200
    print("Testing Passed")


def addTweet():
    login = client.post(
        "/api/login", json={
            "email": "vinaysingh8866@gmail.com",
            "upassword": "123456789"})
    token = login.json['token']
    response = client.post(
        "/api/add_tweet", headers={"Authorization": "Bearer " + token}, json={
            "title": "vinaysingh8866@gmail.com",
            "content": "123456789"})
    assert response.status_code == 200
    print("Testing Passed")


def userTweets():
    login = client.post(
        "/api/login", json={
            "email": "vinaysingh8866@gmail.com",
            "upassword": "123456789"})
    token = login.json['token']
    response = client.post(
        "/api/user_tweets", headers={"Authorization": "Bearer " + token}, json={
            "uid": 1})
    assert response.status_code == 200
    print("Testing Passed")


def updateTweet():
    login = client.post(
        "/api/login", json={
            "email": "vinaysingh8866@gmail.com",
            "upassword": "123456789"})
    token = login.json['token']
    response = client.post(
        "/api/update_tweet/1", headers={"Authorization": "Bearer " + token}, json={
            "content": "123jhbljb456789kjhfkjhf"})
    assert response.status_code == 200
    print("Testing Passed")

def test():
    print("--------------Testing Register---------------")
    testRegister()
    print("--------------Testing Login--------------")
    testLogin()
    print("--------------Testing Add Tweet--------------")
    addTweet()
    print("--------------Testing Update Tweet--------------")
    updateTweet()
    print("--------------Testing User Tweets--------------")
    userTweets()

test()