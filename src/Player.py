import re
from decimal import Decimal


class Player:
    _cash: Decimal = 0.0
    _compost: Decimal = 0.0

    def __init__(self, line):
        values = re.split(',', line)
        self._cash = Decimal(values[0])
        self._compost = Decimal(values[1])

    def add_cash(self, amount):
        self._cash += amount

    def add_compost(self, amount):
        self._compost += amount

    def use_cash(self, amount):
        if self._cash >= amount:
            self._cash -= amount

    def use_compost(self, amount):
        if self._compost >= amount:
            self._compost -= amount

    def save_state(self):
        return str(self._cash) + "," + str(self._compost)
