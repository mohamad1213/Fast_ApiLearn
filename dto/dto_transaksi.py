from typing import Optional

from pydantic import BaseModel

from enums.enum_method import MethodModel
from enums.enum_tipe import TipeModel


class TransaksiModel(BaseModel):
    tipe: TipeModel
    amount: int
    notes: Optional[str] = None
    method: MethodModel
    