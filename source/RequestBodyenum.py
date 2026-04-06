from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from enum import Enum
from typing import Optional
app = FastAPI()
# method dalam fast api ada 4 yaitu GET, POST, PUT, DELETE. 
# method ini digunakan untuk menentukan jenis request yang akan dilakukan pada endpoint tertentu.

# QUERY PARAMETER
@app.get("/transaksi")
def get_transaksi(tipe:str, amount: int):
    print(f'tipe transaksi: {tipe}, jumlah: {amount}')
    
    print(type(tipe))
    print(type(amount))
    
    return f'balikin transkasi dengan tipe {tipe} dan jumlah {amount}'

# PATH PARAMETER
@app.get("/transaksi/{tipe}")
def get_transaksi(tipe:str):
    print(f'tipe transaksi: {tipe}')
    
    print(type(tipe))
    
    return f'balikin transkasi dengan tipe {tipe}'



#Request Body
# tipe, amount, notes, method
class TipeModel(str, Enum):
    def __str__(self):
        return str(self.value)
    INCOME = "income"
    EXPENSE = "expense"
    INVESTMENT = "investment"
class MethodModel(str, Enum):
    def __str__(self):
        return str(self.value)
    CASH = "cash"
    BANK_TRANSFER = "bank_transfer"
    EWALLET = "ewallet"
class TransaksiModel(BaseModel):
    tipe: TipeModel
    amount: int
    notes: Optional[str] = None
    method: MethodModel
    
@app.post("/transaksi")
def create_transaksi(input_transaksi:TransaksiModel):
    list_transaksi = []
    list_transaksi.append(input_transaksi)
    return list_transaksi