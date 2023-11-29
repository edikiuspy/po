from src.main import app
from src.main import create_user
from src.main import ping
from src.main import users

CREATED = 204


def test_ping() -> None:
    actual = ping()
    assert "ping" == actual


def test_create_user() -> None:
    payload = {
        "name": "John",
        "lastname": "Doe",
    }
    with app.test_request_context(json=payload):
        actual = create_user()
    assert payload in users
