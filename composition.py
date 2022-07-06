class Cliente:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insert_address(self, cidade, estado):
        self.enderecos.append(Address(cidade, estado))

    def list_address(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)


class Address:
    def __init__(self, cidade, estado) -> None:
        self.cidade = cidade
        self.estado = estado
