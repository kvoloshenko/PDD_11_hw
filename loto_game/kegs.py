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
        k = self.__kegs[self.__i]
        self.__i += 1
        return k

    def get_current(self):
        return self.__i

    def __init__(self):
        self.__kegs = []
        # print (type (self.__kegs))
        self.__i = 0
        # print(f'i={self.__i}')
        self.__kreate_kegs()

# if __name__ == '__main__':
#     k = Kegs()
#     # print(f'k.get_current()={k.get_current()}')
#     kegs = k.get_kegs()
#     print(type(kegs), f' len(kegs)={len(kegs)} kegs={kegs}')
#     keg = kegs[0]
#     print(type(keg), keg.get_num())
#     for kk in kegs:
#         print(f'keg_num={kk.get_num()}')
#     print(f'get_next={k.get_next().get_num()} curent={k.get_current()}')
#     print(f'get_next={k.get_next().get_num()} curent={k.get_current()}')
