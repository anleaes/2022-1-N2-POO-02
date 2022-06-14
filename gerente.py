from funcionario import Funcionario

class Gerente(Funcionario):
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

gerente1 = Gerente('Antonio',8999454,'Gerente',5000.45,20)