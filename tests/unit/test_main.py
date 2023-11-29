import json
import pytest
from src.main import app, create_user, get_users, get_user, update_user, put_user, delete_user


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_create_user(client):
    payload = {
        "name": "Eduard",
        "lastname": "Muntianov",
    }
    response = client.post("/users", json=payload)
    actual = get_users().get_json()
    del actual[-1]["id"]
    assert payload in actual


def test_get_users(client):
    response = client.get("/users")
    assert response.get_json() == get_users().get_json()


def test_get_user(client):
    user_id = 0
    response = client.get(f"/users/{user_id}")
    assert response.get_json() == get_user(user_id).get_json()


def test_update_user(client):
    user_id = 0
    payload = {"name": "Andrzej"}
    response = client.patch(f"/users/{user_id}", json=payload)
    assert get_user(user_id).get_json()["name"] == "Andrzej"


def test_update_user_bad_request(client):
    user_id = 0
    payload = {"aa": "bbb"}
    response = client.patch(f"/users/{user_id}", json=payload)
    assert response.status_code == 400


def test_put_user(client):
    user_id = 0
    payload = {"name": "Wojciech", "lastname": "Oczkowski"}
    assert get_user(user_id).get_json() == payload


def test_delete_user(client):
    user_id = 0
    response = client.delete(f"/users/{user_id}")
    assert len(get_users().get_json()) == 0


def test_delete_user_not_found(client):
    user_id = 100
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 400
