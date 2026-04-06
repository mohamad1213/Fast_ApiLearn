 
from typing import List

from pydantic import parse_obj_as

from config.config import get_db_connection
from pymongo.database import Database
from fastapi import Depends

from dto.dto_transaksi import TransaksiModel
from model.model_transaksi import TransaksiModelMongo 

class RepositoryTransaksi:
    def __init__(self, db:Database = Depends(get_db_connection)) -> None:
        self.repository = db.get_collection("transaksi")
        
    def insert_new_transaksi(self, transaksi_data:TransaksiModel):
        result = self.repository.insert_one(transaksi_data.dict())
        return result.inserted_id
    def get_list_transaksi(self, match_filter:dict):
        result_filter = self.repository.find(match_filter)
        list_result = list(result_filter)
        return parse_obj_as(List[TransaksiModelMongo], list_result)