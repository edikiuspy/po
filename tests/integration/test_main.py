from flask import Flask, Response, request, jsonify
import pytest
from src.main import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_get_users(client):
    response = client.get("/users")
    assert response.status_code == 200


def test_create_user(client):
    data = {'name': 'Eduard', 'lastname': 'Muntianov'}
    response = client.post("/users", json=data)
    assert response.status_code == 201


def test_get_user(client):
    response = client.get("/users/0")
    assert response.status_code == 200


def test_update_user(client):
    data = {'name': 'Aduard'}
    response = client.patch("/users/0", json=data)
    assert response.status_code == 204


def test_put_user(client):
    data = {'id': 0, 'name': 'Aduard', 'lastname': 'Mantanov'}
    response = client.put("/users/0", json=data)
    assert response.status_code == 204


def test_delete_user(client):
    response = client.delete("/users/0")
    assert response.status_code == 204
