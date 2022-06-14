from funcionario import * 

class Vendedor(Funcionario):
    def __init__(self,funcionario,comissao):
        #super().__init__(nome, matricula, cargo, salario)
        self._funcionario = funcionario
        self._comissao = comissao

    
    def nome_funcionario(self):
        print('Funcionario:', funcionario1._nome)
    def matricula(self):
        print('Matricula:', funcionario1._matricula)
    def cargo(self):
        print('Cargo:', funcionario1._cargo)
    def salario(self):
        print('Salario:', funcionario1._salario)
    def comissao(self):
        print('Porcentagem da Comissao:',self._comissao)
    
    def dados(self):
        print('Funcionario:', funcionario1._nome)
        print('Matricula:', funcionario1._matricula)
        print('Cargo:', funcionario1._cargo)
        print('Salario:', funcionario1._salario)
        print('Porcentagem da Comissao:',self._comissao)

vendedor1 = Vendedor(funcionario1,10)


