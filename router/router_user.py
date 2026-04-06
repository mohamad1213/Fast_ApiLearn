from http.client import HTTPException

from fastapi import APIRouter
from typing import List

from fastapi.params import Depends

from dto.dto_user import InputLogin, InputUser
from service.service_user import ServiceUser

router_user = APIRouter(
    prefix="/api/v1", tags=["user"])

@router_user.post("/user")
def register(input_user: InputUser, service_user: ServiceUser = Depends()):
    return service_user.register_user(input_user)

@router_user.post("/login")
def login(input_login: InputLogin, service_user: ServiceUser = Depends()):
    user = service_user.login_user(input_login)
    if user is None:
        raise HTTPException(401, "Invalid username or password")
    return user