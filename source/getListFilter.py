from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from enum import Enum
from typing import Optional
app = FastAPI()
# method dalam fast api ada 4 yaitu GET, POST, PUT, DELETE. 
# method ini digunakan untuk menentukan jenis request yang 
# akan dilakukan pada endpoint tertentu.
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
    
list_transaksi = []
@app.post("/transaksi")
def create_transaksi(input_transaksi:TransaksiModel):
    list_transaksi.append(input_transaksi)
    return list_transaksi

# Get List filter 

@app.get("/transaksi")
def get_filter_transaksi(tipe:Optional[TipeModel] = None):
    if tipe is not None:
        result_filter = []
        for t in list_transaksi:
            t = TransaksiModel.parse_obj(t)
            if t.tipe == tipe:
                result_filter.append(t)
    else:
        result_filter = list_transaksi  
    return result_filter
