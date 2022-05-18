from loto_game.keg import Keg

class TestKeg:

    def test_num(self):
        keg = Keg()
        keg.set_num(99)
        assert keg.get_num() == 99
