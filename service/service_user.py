from typing import List, Optional

from fastapi.params import Depends
from dto.dto_user import InputLogin, InputUser
from repository.repository_user import RepositoryUser


class ServiceUser:
    def __init__(self, repository_user:RepositoryUser = Depends()) -> None:
        self.repository_user = repository_user
    def register_user(self, input_user:InputUser):
        return self.repository_user.register_user(input_user)
    
    def login_user(self, input_login:InputLogin):
        return self.repository_user.find_user_by_username_password(input_login)
    