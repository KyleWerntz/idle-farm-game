import unittest
import time
from src import Crop
from src.crops import Carrot
from src import Upgrade
from decimal import Decimal


class MyTestCase(unittest.TestCase):
    def test_getters(self):
        c = Crop.Crop('Carrot,10,103,5,10,1,0.5,25.3,10,3,1.5,0.07,.42')
        self.assertEqual(c.get_name(), "Carrot")
        self.assertEqual(c.get_number_crop_owned(), 10)
        self.assertEqual(c.get_amount_produced(), 103)
        self.assertEqual(c.get_base_cost(), 5)
        self.assertEqual(c.get_base_growth_time(), 10)
        self.assertEqual(c.get_base_sell_value(), 1)
        self.assertEqual(c.get_base_compost_value(), 0.5)
        self.assertAlmostEqual(c.get_current_cost(), Decimal(25.3))
        self.assertEqual(c.get_current_growth_time(), 10)
        self.assertEqual(c.get_current_sell_value(), 3)
        self.assertEqual(c.get_current_compost_value(), Decimal(1.5))
        self.assertAlmostEqual(c.get_rate_cost_growth(), Decimal(.07))

    def test_apply_upgrade(self):
        u = Upgrade.Upgrade("Test Upgrade,sell,3,False")
        c = Crop.Crop('Carrot,10,103,5,10,1,0.5,25.3,10,1,0.5,0.07,.42')
        c.apply_upgrade(u)
        self.assertAlmostEqual(c.get_current_sell_value(), 3)
        self.assertEqual(True, u.is_purchased())
        u = Upgrade.Upgrade("Test Upgrade,compost,3,False")
        c.apply_upgrade(u)
        self.assertAlmostEqual(c.get_current_compost_value(), 1.5)
        u = Upgrade.Upgrade("Test Upgrade,time,2,False")
        c.apply_upgrade(u)
        self.assertAlmostEqual(c.get_current_growth_time(), 5)

    def test_sell_produce(self):
        c = Crop.Crop('Carrot,10,103,5,10,1,0.5,25.3,10,1,0.5,0.07,.42')
        actual = c.sell_produce()
        self.assertEqual(0, c.get_amount_produced())
        self.assertEqual(103, actual)

    def test_compost_produce(self):
        c = Crop.Crop('Carrot,10,103,5,10,1,0.5,25.3,10,1,0.5,0.07,.42')
        actual = c.compost_produce()
        self.assertEqual(0, c.get_amount_produced())
        self.assertAlmostEqual(Decimal(51.5), actual)

    def test_produce(self):
        c = Crop.Crop('Carrot,10,103,5,10,1,0.5,25.3,.1,1,0.5,0.07,0')
        time.sleep(2)
        c.produce()
        self.assertEqual(123, c.get_amount_produced())
        self.assertTrue(c.get_leftover_crops() < 1)

    def test_default_carrot(self):
        c = Carrot.Carrot("", create_new=True)
        self.assertEqual(c.get_name(), "0")


if __name__ == '__main__':
    unittest.main()
