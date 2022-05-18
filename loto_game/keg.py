
class Keg:
    def __init__(self):
        self.__num = 0

    def set_num(self, num):
        self.__num = num

    def get_num(self):
        return self.__num

# if __name__ == '__main__':
#     keg_1 = Keg()
#     print(f'keg_1.get_num()={keg_1.get_num()}')
#     keg_1.set_num(99)
#     print(f'keg_1.get_num()={keg_1.get_num()}')
