from fastapi import Depends
from pymongo.database import Database
from config.config import get_db_connection
from dto.dto_user import InputLogin, InputUser
from model.model_user import User

class RepositoryUser:
    def __init__(self, db: Database = Depends(get_db_connection)):
        self.db = db

    def register_user(self, input_user: InputUser):
        user_data = input_user.dict()
        self.db.users.insert_one(user_data)
        return {"message": "User registered successfully"}
    def find_user_by_username_password(self, input_login: InputLogin):
        user = self.db.users.find_one({"username": input_login.username, "password": input_login.password})
        if user is not None:
            return User.parse_obj(user)
        return None