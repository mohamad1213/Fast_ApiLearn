from enum import Enum
class TipeModel(str, Enum):
    def __str__(self):
        return str(self.value)
    INCOME = "income"
    EXPENSE = "expense"
    INVESTMENT = "investment"