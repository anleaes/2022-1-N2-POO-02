from asyncio.windows_events import NULL
from pickle import TRUE


class Veiculo:
    def __init__(self,marca,modelo,ano,cor,disponivel):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._cor = cor
        self._disponivel = disponivel
        
    #Especificações separadas caso queira chamar apenas uma
    def marca(self):
        print("Marca desejada:", self._marca)
    def modelo(self):
        print("Modelo desejado:", self._modelo)
    def ano(self):
        print("Ano:", self._ano)
    def cor(self):
        print('Cor escolhida:', self._cor)

    #Especificações juntas para chamar com apenas uma linha de comando
    def especificacoes(self):
        print("\nMarca desejada:", self._marca)
        print("Modelo desejado:", self._modelo)
        print("Ano:", self._ano)
        print('Cor escolhida:', self._cor)
    

    
    def disponivel(self):
        if self._disponivel == TRUE:
            print("Carro disponivel")
        else:
            print("Carro indisponivel")

veiculo1 = Veiculo('Toyota', 'Etios', 2016,'Vermelho', NULL)
veiculo2 = Veiculo('Audi', 'A3', 2020, 'prata', TRUE)