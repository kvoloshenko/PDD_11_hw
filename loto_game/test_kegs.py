from loto_game.kegs import Kegs

class TestKegs:

    def test_get_kegs(self):
        k = Kegs()
        kegs = k.get_kegs()
        assert len(kegs) == 90

    def test_get_next(self):
        k = Kegs()
        kegs = k.get_kegs()
        num = k.get_next().get_num()
        assert num > 0 and num <= 90

    def test_get_current(self):
        k = Kegs()
        assert k.get_current() == 0
        k.get_next()
        assert k.get_current() == 1