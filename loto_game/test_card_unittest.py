import unittest
from loto_game.card import Card_line
from loto_game.card import Card
from loto_game.kegs import Kegs

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

    def test_card_line_eq(self):
        card_line_1 = Card_line()
        card_line_1.set_nums([1, 2, 3, 4, 5])
        card_line_2 = Card_line()
        card_line_2.set_nums([5, 4, 3, 2, 1])
        self.assertEqual(card_line_1,card_line_1)
        self.assertNotEqual(card_line_1,card_line_2)

    def test_card_line_contains(self):
        card_line_1 = Card_line()
        card_line_1.set_nums([1, 2, 3, 4, 5])
        self.assertTrue(card_line_1.__contains__(5))
        self.assertFalse(card_line_1.__contains__(7))

    def test_card_is_crossed(self):
        crd = Card()
        k = Kegs()
        while k.get_current() < 90:
            num = k.get_next().get_num()
            # print(num)
            crd.cross_out(num)
        # crd.print_card()
        self.assertTrue(crd.is_crossed())

    def test_set_header(self):
        crd = Card()
        header = 'Test string'
        crd.set_header(header)
        self.assertIn(header, str(crd))
