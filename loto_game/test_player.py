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
