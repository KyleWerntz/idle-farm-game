import re
from decimal import Decimal


class Player:

    def __init__(self, line: str, create_new=False):
        if create_new:
            values = [0,0]
        else:
            values = re.split(',', line)
        self._cash = Decimal(values[0])
        self._compost = Decimal(values[1])

    def get_cash(self):
        return self._cash

    def get_compost(self):
        return self._compost

    def add_cash(self, amount: Decimal):
        if amount >= 0:
            self._cash += amount

    def add_compost(self, amount: Decimal):
        if amount >= 0:
            self._compost += amount

    def use_cash(self, amount: Decimal):
        if self._cash >= amount >= 0:
            self._cash -= amount

    def use_compost(self, amount: Decimal):
        if self._compost >= amount >= 0:
            self._compost -= amount

    def save_state(self):
        return f"{str(self._cash)} + ',' + {str(self._compost)}"
