class Funcionario:
    def __init__(self, nome, matricula, cargo, salario):
        self._nome = nome
        self._matricula = matricula
        self._cargo = cargo
        self._salario = salario   
    
    
    def nome_funcionario(self):
        print('Funcionario:', self._nome)
    def matricula(self):
        print('Matricula:', self._matricula)
    def cargo(self):
        print('Cargo:', self._cargo)
    def salario(self):
        print('Salario:', self._salario)
    
funcionario1 = Funcionario('Joao', 99995612,'Vendedor', 1300.00)
funcionario2 = Funcionario('Antonio',8999454,'Gerente',5000.45)