from math import floor, log, pow
from datetime import datetime
from decimal import Decimal
from src import Upgrade


class Crop:

    def __init__(self, line: str):
        values = line.split(',')
        self._date_format = '%Y-%m-%d %H:%M:%S'

        self._name = values[0]
        self._crops_owned = Decimal(values[1])
        self._amount_produced = Decimal(values[2])
        self._base_cost = Decimal(values[3])
        self._base_growth_time = Decimal(values[4])
        self._base_sell_value = Decimal(values[5])
        self._base_compost_value = Decimal(values[6])
        self._current_cost = Decimal(values[7])
        self._current_growth_time = Decimal(values[8])
        self._current_sell_value = Decimal(values[9])
        self._current_compost_value = Decimal(values[10])
        self._rate_cost_growth = Decimal(values[11])
        self._crops_produced_leftovers = Decimal(values[12])
        if values[13] == "0":
            self._previous_time = Decimal(datetime.utcnow().timestamp())
        else:
            self._previous_time = Decimal(values[13])
        self.produce()

    def get_name(self):
        return self._name

    def get_number_crop_owned(self):
        return self._crops_owned

    def get_amount_produced(self):
        return self._amount_produced

    def get_base_cost(self):
        return self._base_cost

    def get_base_growth_time(self):
        return self._base_growth_time

    def get_base_sell_value(self):
        return self._base_sell_value

    def get_base_compost_value(self):
        return self._base_compost_value

    def get_current_cost(self):
        return self._current_cost

    def get_current_growth_time(self):
        return self._current_growth_time

    def get_current_sell_value(self):
        return self._current_sell_value

    def get_current_compost_value(self):
        return self._current_compost_value

    def get_rate_cost_growth(self):
        return self._rate_cost_growth

    def get_leftover_crops(self):
        return self._crops_produced_leftovers

    def get_cost_of_next(self):
        return self._base_cost * Decimal((pow(self._rate_cost_growth, self._crops_owned)))

    def get_cost_of_x(self, x):
        return self._base_cost * (pow(self._rate_cost_growth, self._crops_owned)) * \
                    ((pow(self._rate_cost_growth, x)) - 1) / (self._rate_cost_growth - 1)

    def get_cost_of_max(self, cash):
        return floor(log(((cash * (self._rate_cost_growth - 1)) / self.get_cost_of_next()) + 1, self._rate_cost_growth))

    def apply_upgrade(self, upgrade: Upgrade):
        if upgrade.get_type() == "sell":
            self._current_sell_value *= upgrade.get_value()
        elif upgrade.get_type() == "compost":
            self._current_compost_value *= upgrade.get_value()
        elif upgrade.get_type() == "time":
            self._current_growth_time /= upgrade.get_value()
        upgrade.purchase()

    def sell_produce(self):
        cash_earned = self.get_potential_sell()
        self._amount_produced = 0
        return cash_earned

    def get_potential_sell(self):
        return self._amount_produced * self._current_sell_value

    def get_potential_compost(self):
        return self._amount_produced * self._current_compost_value

    def compost_produce(self):
        cash_earned = self.get_potential_compost()
        self._amount_produced = 0
        return cash_earned

    def produce(self):
        current_time = Decimal(datetime.utcnow().timestamp())
        time_passed = current_time - self._previous_time
        self._previous_time = current_time
        just_produced = (time_passed / self._current_growth_time) + self._crops_produced_leftovers
        self._amount_produced += int(just_produced)
        self._crops_produced_leftovers = just_produced % 1

    def save_state(self):
        return f"{str(self._name)},{str(self._crops_owned)},{str(self._amount_produced)},{str(self._base_cost)}," \
               f"{str(self._base_growth_time)},{str(self.get_base_sell_value())},{str(self._base_compost_value)}," \
               f"{str(self._current_cost)},{str(self._current_growth_time)},{str(self._current_sell_value)}," \
               f"{str(self._current_compost_value)},{str(self._rate_cost_growth)}," \
               f"{str(self._crops_produced_leftovers)},{str(self._previous_time)}"
