from loto_game.keg import Keg
import random


class Kegs:

    def __kreate_kegs(self):
        for i in range(1, 91):
            keg = Keg()
            keg.set_num(i)
            # print(f'keg.get_num()={keg.get_num()}')
            self.__kegs.append(keg)
        random.shuffle(self.__kegs)

    def get_kegs(self):
        return self.__kegs

    def get_next(self):
        # print(f' i before get_nex={self.__i}')
        keg = self.__kegs[self.__i]
        self.__i += 1
        return keg

    def get_current(self):
        return self.__i

    def __init__(self):
        self.__kegs = []
        # print (type (self.__kegs))
        self.__i = 0
        # print(f'i={self.__i}')
        self.__kreate_kegs()

    def __str__(self):
        s = ''
        i = 0
        for keg in self.__kegs:
            s += str(keg)
            if i < 89:
                s += ', '
                i+=1
        return s

    def __len__(self):
        return len(self.__kegs)

    def __getitem__(self, item):
        return self.__kegs[item]

    def __eq__(self, other):
        return str(self) == str(other)


# if __name__ == '__main__':
#     k = Kegs()
#     print(f'k = {k}')
#     print(f'len of kegs={len(k)}')
#     print(k[1])
#     k2 = Kegs()
#     print(f'k2 = {k2}')
#     print(f'k2 = {k2}')
#     print(k == k)
#     print(k == k2)
#     print(f'k.get_current()={k.get_current()}')
#     kegs = k.get_kegs()
#     print(type(kegs), f' len(kegs)={len(kegs)} kegs={kegs}')
#     keg = kegs[0]
#     print(type(keg), keg.get_num())
#     for kk in kegs:
#         print(f'keg_num={kk.get_num()}')
#     print(f'get_next={k.get_next().get_num()} curent={k.get_current()}')
#     print(f'get_next={k.get_next().get_num()} curent={k.get_current()}')
