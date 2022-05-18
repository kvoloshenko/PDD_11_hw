from loto_game.card import Card


class Player:

    def set_card(self, card):
        self.__card = card

    def get_card(self):
        return self.__card

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_type(self, type):
        self.__type = type

    def get_type(self):
        return self.__type

    def __init__(self):
        self.set_type('Human')
        self.set_card(Card())

    def __str__(self):
        return f'type={self.__type} name={self.__name}'

    def __eq__(self, other):
        if self.__name == other.__name and self.__type == other.__type:
            return True
        else:
            return False


# if __name__ == '__main__':
#     players = []
#     p = Player()
#     p.set_name('Константин')
#     print(f'Player: {p}')
#     p1 = Player()
#     p1.set_name('Константин')
#     c1 = p1.get_card()
#     c1.set_header('------ Ваша карточка ----------')
#     print(p == p1)
#
#     players.append(p1)
#
#     p2 = Player()
#     p2.set_name('Компьютер')
#     p2.set_type('computer')
#     c2 = p2.get_card()
#     c2.set_header('---- Карточка компьютера ------')
#     players.append(p2)
#     print(p == p2)
#
#     for player in players:
#         print(f'{player.get_name()}')
#         crd = player.get_card()
#         crd.print_card()
