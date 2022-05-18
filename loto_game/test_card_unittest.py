import unittest
from loto_game.card import Card_line

class TestCard(unittest.TestCase):
    def test_card_line_set_nums(self):
        card_line = Card_line()
        card_line.set_nums([1,2,3,4,5])
        new_nums = card_line.get_nums()
        # print(f'new_nums={new_nums}')
        self.assertIn(0, new_nums)
        self.assertIn(1, new_nums)
        self.assertIn(2, new_nums)
        self.assertIn(3, new_nums)
        self.assertIn(4, new_nums)
        self.assertIn(5, new_nums)
        # print(f'len(new_nums)={len(new_nums)}')
        test_l = [1, 2, 0, 0, 3, 4, 5, 0, 0]
        self.assertCountEqual(test_l, new_nums)
