from typing import List, Optional

from fastapi.params import Depends
from pydantic import parse_obj_as

from model.model_transaksi import TransaksiModelMongo
from repository.repository_transaksi import RepositoryTransaksi
from source.getListFilter import TipeModel, TransaksiModel


class ServiceTransaksi:
    def __init__(self, repository_transaksi:RepositoryTransaksi = Depends()) -> None:
        self.repository_transaksi = repository_transaksi
    def insert_new_transaksi(self, transaksi_data:TransaksiModel):
        return self.repository_transaksi.insert_new_transaksi(transaksi_data)
    def get_list_transaksi(self, tipe:Optional[TipeModel] = None):
        match_filter = {}
        if tipe is not None:
            match_filter ['tipe'] = tipe
        return self.repository_transaksi.get_list_transaksi(match_filter)
    