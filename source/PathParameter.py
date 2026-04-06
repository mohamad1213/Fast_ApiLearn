from fastapi import FastAPI
import uvicorn

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

