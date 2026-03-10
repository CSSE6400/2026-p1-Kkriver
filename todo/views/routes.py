from flask import Blueprint, jsonify, request

api = Blueprint("api", __name__, url_prefix="/api/v1")

TODOS = [
    {
        "id": 1,
        "title": "Sample todo",
        "description": "This is a sample todo",
        "completed": False,
        "deadline_at": None,
    }
]

ALLOWED_FIELDS = {"title", "description", "completed", "deadline_at"}


@api.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


@api.get("/todos")
def list_todos():
    return jsonify(TODOS), 200


@api.get("/todos/<int:todo_id>")
def get_todo(todo_id: int):
    for todo in TODOS:
        if todo["id"] == todo_id:
            return jsonify(todo), 200
    return jsonify({"error": "Not found"}), 404


@api.post("/todos")
def create_todo():
    data = request.get_json(silent=True) or {}

    extra_fields = set(data.keys()) - ALLOWED_FIELDS
    if extra_fields:
        return jsonify({"error": "Invalid fields"}), 400

    title = data.get("title")
    if not title:
        return jsonify({"error": "title is required"}), 400

    new_id = max(todo["id"] for todo in TODOS) + 1 if TODOS else 1

    new_todo = {
        "id": new_id,
        "title": title,
        "description": data.get("description"),
        "completed": data.get("completed", False),
        "deadline_at": data.get("deadline_at"),
    }

    TODOS.append(new_todo)
    return jsonify(new_todo), 201


@api.put("/todos/<int:todo_id>")
def update_todo(todo_id: int):
    data = request.get_json(silent=True) or {}

    extra_fields = set(data.keys()) - ALLOWED_FIELDS
    if extra_fields:
        return jsonify({"error": "Invalid fields"}), 400

    for todo in TODOS:
        if todo["id"] == todo_id:
            for field in ALLOWED_FIELDS:
                if field in data:
                    todo[field] = data[field]
            return jsonify(todo), 200

    return jsonify({"error": "Not found"}), 404


@api.delete("/todos/<int:todo_id>")
def delete_todo(todo_id: int):
    global TODOS
    TODOS = [todo for todo in TODOS if todo["id"] != todo_id]
    return "", 200