from veiculo import *

class Seguro(Veiculo):
    def __init__(self, veiculo, valor, tempo):
        # super().__init__(modelo, ano, cor, disponivel)
        self._veiculo = veiculo
        self._valor = valor
        self._tempo = tempo
    
    def valor(self):
        print("Valor total do seguro:", self._valor)
    def tempo(self):
        print("Tempo de duracao do seguro:", self._tempo)
    
    def contrato(self):
        print("Valor total do seguro:", self._valor)
        print("Tempo de duracao do seguro:", self._tempo)


seguro1 = Seguro(veiculo1,1000, '1 mes')