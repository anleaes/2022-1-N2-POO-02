from funcionario import Funcionario 

class Vendedor(Funcionario):
    def __init__(self, nome, matricula, cargo, salario, comissao):
        super().__init__(nome, matricula, cargo, salario)
        self._comissao = comissao