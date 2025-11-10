from models.user import User
from database.user import user_service

def create_user(username,password):
        user = User(username,password)
        user_service.insert(user)
        print(f"User {username} created successfully.")