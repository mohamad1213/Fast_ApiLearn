from fastapi.exceptions import HTTPException  # Correct import for HTTPException
from typing import List, Optional

from fastapi.params import Depends
from dto.dto_user import InputLogin, InputUser
from repository.repository_user import RepositoryUser
from service import service_security


class ServiceUser:
    def __init__(self, repository_user:RepositoryUser = Depends()) -> None:
        self.repository_user = repository_user
        self.service_security = service_security # hasing password and generate token
    def register_user(self, input_user:InputUser):
        found_duplicate_user = self.repository_user.find_user_by_username(input_user.username)
        if found_duplicate_user is not None:
            raise HTTPException(status_code=400, detail="Username already exists")
        ## hasing
        input_user.password = self.service_security.get_password_hash(input_user.password)
        return self.repository_user.register_user(input_user)
    
    def login_user(self, input_login:InputLogin):
        found_user = self.repository_user.find_user_by_username(input_login.username)
        if found_user is None:
            raise HTTPException(404, "Username not found")
        if not self.service_security.verify_password(input_login.password, found_user.password):
            raise HTTPException(401, "Invalid username or password")
        return found_user
