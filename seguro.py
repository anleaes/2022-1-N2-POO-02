from veiculo import Veiculo

class Seguro(Veiculo):
    def __init__(self, modelo, ano, cor, disponivel, valor, tempo):
        super().__init__(modelo, ano, cor, disponivel)
        self._valor = valor
        self._tempo = tempo