import re, math
from datetime import datetime
from decimal import Decimal


class Crop:

    def __init__(self, line):
        values = re.split(',', line)
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
        self._time_to_next_production = Decimal(values[12])
        self._previous_time = datetime.strptime(values[13], self._date_format)
        self._crops_produced_leftovers = 0.0

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

    def get_time_to_next_production(self):
        return self._time_to_next_production

    def get_cost_of_next(self):
        return self._base_cost * (math.pow(self._rate_cost_growth, self._crops_owned))

    def get_cost_of_x(self, x):
        return self._base_cost * (math.pow(self._rate_cost_growth, self._crops_owned)) * \
                    ((math.pow(self._rate_cost_growth, x)) - 1) / (self._rate_cost_growth - 1)

    def get_cost_of_max(self, cash):
        return math.floor(math.log(((cash * (self._rate_cost_growth - 1)) /
                                    self.get_cost_of_next()) + 1, self._rate_cost_growth))

    def apply_upgrade(self, upgrade):
        if upgrade.get_type() == "sell":
            self._current_sell_value *= upgrade.get_value()
        elif upgrade.get_type() == "compost":
            self._current_compost_value *= upgrade.get_value()
        elif upgrade.get_type() == "time":
            self._current_growth_time /= upgrade.get_value()
        upgrade.purchase()

    def sell_produce(self):
        cash_earned = self._amount_produced * self._current_sell_value
        self._amount_produced = 0
        return cash_earned

    def compost_produce(self):
        cash_earned = self._amount_produced * self._current_compost_value
        self._amount_produced = 0
        return cash_earned

    def produce_over(self, current_time_unformatted):
        current_time = datetime.strptime(current_time_unformatted, self._date_format)
        time_passed = current_time - self._previous_time
        self._previous_time = current_time
        microseconds = time_passed.microseconds
        just_produced = (microseconds / self._current_growth_time) + self._crops_produced_leftovers
        self._amount_produced += int(just_produced)
        self._crops_produced_leftovers = just_produced % 1


