import unittest
from src import Player


class MyTestCase(unittest.TestCase):
    def test_add_cash(self):
        p = Player.Player('0,0')
        p.add_cash(100)
        expected = 100
        self.assertEqual(expected, p.get_cash())

        p.add_cash(-1)
        expected = 100
        self.assertEqual(expected, p.get_cash())

    def test_add_compost(self):
        p = Player.Player('0,0')
        p.add_compost(100)
        expected = 100
        self.assertEqual(expected, p.get_compost())

        p.add_compost(-1)
        expected = 100
        self.assertEqual(expected, p.get_compost())

    def test_use_cash(self):
        p = Player.Player('100,0')
        p.use_cash(101)
        expected = 100
        self.assertEqual(expected, p.get_cash())

        p.use_cash(-1)
        self.assertEqual(expected, p.get_cash())

        p.use_cash(99)
        expected = 1
        self.assertEqual(expected, p.get_cash())

    def test_use_compost(self):
        p = Player.Player('0,100')
        p.use_compost(101)
        expected = 100
        self.assertEqual(expected, p.get_compost())

        p.use_compost(-1)
        self.assertEqual(expected, p.get_compost())

        p.use_compost(99)
        expected = 1
        self.assertEqual(expected, p.get_compost())


if __name__ == '__main__':
    unittest.main()
