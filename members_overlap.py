""" Sobreposição de Métodos na Herança Simples"""


class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        self.nomeclass = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclass} falando...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclass} comprando...')

    def falar(self):
        print('Estou em CLIENTE.')


# Tudo que tem em Cliente tem em clienteVip
# Tudo que tem em Pessoa Também tem em ClienteVip
class ClienteVip(Cliente):
    # Sobrepor o construtor da super classe(Pessoa)
    def __init__(self, nome, idade, sobrenome) -> None:
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    # Sobrescrevendo o método (sobreposição)
    def falar(self):
        # super().falar()
        # Outra forma de fazer
        Pessoa.falar(self)  # Chama falar da classe Pessoa
        Cliente.falar(self)  # Chama falar da classe Cliente
        print(f'{self.nome} {self.sobrenome}')
