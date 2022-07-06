from datetime import datetime


class Animal:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def get_ano_nascimeto(self):
        print(self.ano_atual - self.idade)

    # Método de classe
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


animal1 = Animal.por_ano_nascimento('Bob', 2017)
print(animal1)
print(animal1.nome, animal1.idade)
animal1.get_ano_nascimeto()
