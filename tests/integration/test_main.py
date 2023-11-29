from src.main import app, users

STATUS_OK = 200
CREATED = 204


def test_ping_endpoint() -> None:
    client = app.test_client()
    actual = client.get("/ping")
    assert actual.status_code == STATUS_OK


def test_create_user_endpoint() -> None:
    client = app.test_client()
    payload = {
        "name": "Alice",
        "lastname": "Cee",
    }
    actual = client.post("/users", json=payload)
    print(users)
    assert actual.status_code == CREATED
