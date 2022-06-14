from funcionario import Funcionario 

class Vendedor(Funcionario):
    def __init__(self, nome, matricula, cargo, salario, comissao):
        super().__init__(nome, matricula, cargo, salario)
        self._comissao = comissao
    
    def nome_funcionario(self):
        print('Funcionario:', self._nome)
    def matricula(self):
        print('Matricula:', self._matricula)
    def cargo(self):
        print('Cargo:', self._cargo)
    def salario(self):
        print('Salario:', self._salario)
    def comissao(self):
        print('Porcentagem da Comissao:',self._comissao)

vendedor1 = Vendedor('Joao', 99995612,'Vendedor', 1300.00, 10)