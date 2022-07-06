from random import randint


class Animal:
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand


print(Animal.gera_id())
