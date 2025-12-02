from flask import Blueprint, request, jsonify
from src.services.user_service import *

user_bp = Blueprint("users", __name__)

@user_bp.get("/")
def list_users():
    print("User called")
    users = get_all_users()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])

@user_bp.post("/")
def add_user():
    data = request.json
    user = create_user(data["name"], data["email"])
    return jsonify({"message": "User Created", "id": user.id})

@user_bp.put("/<int:id>")
def edit_user(id):
    data = request.json
    update_user(id, data["name"], data["email"])
    return jsonify({"message": "User Updated"})

@user_bp.delete("/<int:id>")
def remove_user(id):
    delete_user(id)
    return jsonify({"message": "User Deleted"})
