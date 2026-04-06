from typing import Optional

from fastapi import APIRouter, Depends

from enums.enum_tipe import TipeModel
from service.service_transaksi import ServiceTransaksi
from source.getListFilter import TransaksiModel

router_transaksi = APIRouter(
    prefix="/api/v1",tags=["transaksi"])

@router_transaksi.post("/transaksi")
def insert_new_transaksi(input_transaksi: TransaksiModel, service_transaksi: ServiceTransaksi = Depends(),):
    service_transaksi.insert_new_transaksi(input_transaksi)
    return input_transaksi

@router_transaksi.get("/transaksi")
def get_list_transaksi(tipe:Optional[TipeModel] = None, service_transaksi: ServiceTransaksi = Depends()):
    return service_transaksi.get_list_transaksi(tipe)