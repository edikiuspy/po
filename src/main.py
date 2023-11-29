from flask import Flask
from flask import Response
from flask import request

app = Flask(__name__)
users = []


@app.get("/ping")
def ping() -> str:
    return "ping"


@app.post("/users")
def create_user() -> Response:
    users.append(request.json)
    return Response(status=204)
