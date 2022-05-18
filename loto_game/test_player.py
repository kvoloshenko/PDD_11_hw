from loto_game.player import Player
from loto_game.card import Card


class TestPlayer:

    def test_get_card(self):
        p = Player()
        c = p.get_card()
        crd = Card()
        assert type(c) == type(crd)

    def test_set_card(self):
        p = Player()
        c = Card()
        p.set_card(c)
        assert p.get_card() == c

    def test_default_type(self):
        p = Player()
        assert p.get_type() == 'Human'

    def test_set_type(self):
        p = Player()
        type = 'Test_type'
        p.set_type(type)
        assert p.get_type() == type

    def test_name(self):
        p = Player()
        name = 'Test_name'
        p.set_name(name)
        assert p.get_name() == name

    def test_str(self):
        p = Player()
        name = 'Test_name'
        p.set_name(name)
        assert f'type={p.get_type()} name={p.get_name()}' == str(p)

    def test_eq(self):
        p1 = Player()
        p1.set_name('Test_name 1')
        p2 = Player()
        p2.set_name('Test_name 2')
        assert p1 == p1
        assert not p1 == p2


