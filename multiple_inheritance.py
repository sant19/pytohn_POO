""" HERANÇA MULTIPLA """
from log_multiple_inheritace import LogMaxin


class Eletronico:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            return
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            return
        self._ligado = False


class SmartPhone(Eletronico, LogMaxin):
    def __init__(self, nome) -> None:
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info = f'{self.nome} não está ligado.'
            print(info)
            self.log_error(info)
            return

        if self._conectado:
            error = f'{self.nome} JÁ ESTÁ CONECTADO.'
            print(error)
            self.log_error(error)
            return

        info = f'{self.nome} ESTÁ CONECTADO'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self.nome} NÃO ESTÁ CONECTQADO'
            print(error)
            self.log_error(error)
            return

        info = f'{self.nome} foi desligado com sucesso.'
        print(info)
        self.log_info(info)
        self._conectado = False
