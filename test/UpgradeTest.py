import unittest
from src import Upgrade


class MyTestCase(unittest.TestCase):
    def test_getters(self):
        u = Upgrade.Upgrade("Test Upgrade,sell,3,False")
        self.assertEqual("Test Upgrade", u.get_name())
        self.assertEqual("sell", u.get_type())
        self.assertEqual(3, u.get_value())
        self.assertEqual(False, u.is_purchased())
        u = Upgrade.Upgrade("Test Upgrade,value,3,True")
        self.assertEqual(True, u.is_purchased())

    def test_purchase(self):
        u = Upgrade.Upgrade("Test Upgrade,sell,3,False")
        u.purchase()
        self.assertEqual(True, u.is_purchased())


if __name__ == '__main__':
    unittest.main()
