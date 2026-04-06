from fastapi import FastAPI

from router import router_transaksi
from router.router_user import router_user
from router.router_transaksi import *
app = FastAPI()

app.include_router(router_transaksi)
app.include_router(router_user)