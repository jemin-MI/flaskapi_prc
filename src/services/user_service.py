from src.extensions import db
from src.models.user import User

def get_all_users():
    return User.query.all()

def create_user(name, email):
    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()
    return user

def update_user(id, name, email):
    user = User.query.get(id)
    user.name = name
    user.email = email
    db.session.commit()
    return user

def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
