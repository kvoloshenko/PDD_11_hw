
class Keg:
    def __init__(self):
        self.__num = 0

    def set_num(self, num):
        self.__num = num

    def get_num(self):
        return self.__num

    def __str__(self):
        return str(self.__num)

    def __eq__(self, other):
        return self.__num == other.__num

if __name__ == '__main__':
    keg_1 = Keg()
    print(f'keg_1={keg_1}')
    keg_2 = Keg()
    keg_2.set_num(99)
    print(f'keg_2={keg_2}')
    print(keg_1 == keg_2)
    keg_1.set_num(99)
    print(keg_1 == keg_2)