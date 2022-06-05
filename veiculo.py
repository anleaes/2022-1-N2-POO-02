from pickle import TRUE


class Veiculo:
    def __init__(self,modelo,ano,cor,disponivel):
        self._modelo = modelo
        self._ano = ano
        self._cor = cor
        self._disponivel = disponivel


    def disponivel(self):
        if self._disponivel == TRUE:
            print("Carro disponivel")
        else:
            print("Carro indisponivel")