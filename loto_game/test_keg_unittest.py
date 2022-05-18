import unittest
from loto_game.keg import Keg

class TestKegNum(unittest.TestCase):
    def test_num(self):
        keg = Keg()
        keg.set_num(99)
        self.assertEqual(keg.get_num(), 99)

