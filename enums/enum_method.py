from enum import Enum
class MethodModel(str, Enum):
    def __str__(self):
        return str(self.value)
    CASH = "cash"
    BANK_TRANSFER = "bank_transfer"
    EWALLET = "ewallet"