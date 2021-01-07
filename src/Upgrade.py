import re
from decimal import Decimal


class Upgrade:

    def __init__(self, line):
        values = re.split(',', line)
        self._name = values[0]
        self._upgradeType = values[1]
        self._value = Decimal(values[2])
        if values[3] == "False":
            self._purchased = False
        else:
            self._purchased = True

    def get_name(self):
        return self._name

    def get_type(self):
        return self._upgradeType

    def get_value(self):
        return self._value

    def is_purchased(self):
        return self._purchased

    def purchase(self):
        self._purchased = True

    def save_state(self):
        return f"{self._name} + ',' + {self._upgradeType} + ',' + {str(self._value)} + ',' + {str(self._purchased)}"
