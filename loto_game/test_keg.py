from loto_game.keg import Keg

class TestKeg:

    def test_num(self):
        keg = Keg()
        keg.set_num(99)
        assert keg.get_num() == 99

    def test_str(self):
        keg = Keg()
        keg.set_num(21)
        assert str(keg.get_num()) == str(keg)

    def test_eq(self):
        keg_1 = Keg()
        keg_2 = Keg()
        keg_2.set_num(99)
        assert keg_1 == keg_1
        assert not keg_1 == keg_2
