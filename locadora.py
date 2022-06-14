from funcionario import Funcionario

class Locadora(Funcionario):
    def __init__(self, nome, matricula, cargo, salario, cnpj, endereco, qtd_veiculos, telefone):
        super().__init__(nome, matricula, cargo, salario)
        self._cnpj = cnpj
        self._endereco = endereco
        self._qtd_veiculos = qtd_veiculos
        self._telefone = telefone