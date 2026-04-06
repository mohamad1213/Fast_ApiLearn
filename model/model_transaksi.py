from enum import Enum
from typing import List
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from enums.enum_method import MethodModel
from enums.enum_tipe import TipeModel
from model.model_common import PyObjectId
class TransaksiModelMongo(BaseModel):
    id: PyObjectId = Field(alias="_id", default=None)
    tipe: TipeModel
    amount: int
    notes: Optional[str] = None
    method: MethodModel
    class Config:
        json_encoders = {ObjectId: str}
    