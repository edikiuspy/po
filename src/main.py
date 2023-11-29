from flask import Flask, Response, request, jsonify

app = Flask(__name__)
users = []


@app.get("/users")
def get_users() -> Response:
    return jsonify(users)


@app.get("/users/<int:id>")
def get_user(id: int) -> Response:
    return jsonify(users[id])


@app.post("/users")
def create_user() -> Response:
    users.append({'id': len(users) + 1, 'name': request.json['name'], 'lastname': request.json['lastname']})
    return Response(status=201)


@app.patch("/users/<int:id>")
def update_user(id: int) -> Response:
    if id < 0 or id >= len(users):
        return Response(status=400)

    if 'name' in request.json:
        users[id]['name'] = request.json['name']
    elif 'lastname' in request.json:
        users[id]['lastname'] = request.json['lastname']
    else:
        return Response(status=400)

    return Response(status=204)


@app.put("/users/<int:id>")
def put_user(id: int) -> Response:
    users[id] = request.json
    return Response(status=204)


@app.delete("/users/<int:id>")
def delete_user(id: int) -> Response:
    if id < 0 or id >= len(users):
        return Response(status=400)
    users.pop(id)
    return Response(status=204)


if __name__ == "__main__":
    app.run()
