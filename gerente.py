from funcionario import *

class Gerente(Funcionario):
    def __init__(self, funcioario,  comissao):
        self._funcionario = funcioario
        self._comissao = comissao
    
    def nome_funcionario(self):
        print('Funcionario:', funcionario2._nome)
    def matricula(self):
        print('Matricula:', funcionario2._matricula)
    def cargo(self):
        print('Cargo:', funcionario2._cargo)
    def salario(self):
        print('Salario:', funcionario2._salario)
    def comissao(self):
        print('Porcentagem da Comissao:',self._comissao)
    
    def dados(self):
        print('Funcionario:', funcionario2._nome)
        print('Matricula:', funcionario2._matricula)
        print('Cargo:', funcionario2._cargo)
        print('Salario:', funcionario2._salario)
        print('Porcentagem da Comissao:',self._comissao)

gerente1 = Gerente(funcionario2,20)