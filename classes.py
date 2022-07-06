from datetime import datetime


class Pessoa:
    # Variável da classe
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False) -> None:
        # Variáveis da instância
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        if not self.falando:
            print(f'{self.nome} não está falando.')

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def falar(self, assunto):
        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return

        if not self.comendo:
            print(f'{self.nome} não está comendo.')

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
