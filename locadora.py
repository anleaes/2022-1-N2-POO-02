class Locadora:
    def __init__(self,nome,cnpj, endereco, qtd_veiculos, telefone):
        self._nome = nome
        self._cnpj = cnpj
        self._endereco = endereco
        self._qtd_veiculos = qtd_veiculos
        self._telefone = telefone

    def nome(self):
        print(self._nome)
    def cnpj(self):
        print("CNPJ:" ,self._cnpj)
    def endereco(self):
        print("Nosso Endereco:", self._endereco)
    def veiculos(self):
        print("Possuimos mais de:", self._qtd_veiculos)
    def contato(self):
        print("Entre em contato conosco pelo teleofne:", self._telefone)
    
    def resumo(self):
        print(self._nome)
        print("CNPJ:" ,self._cnpj)
        print("Nosso Endereco:", self._endereco)
        print("Possuimos mais de:", self._qtd_veiculos)
        print("Entre em contato conosco pelo teleofne:", self._telefone)

locadora1 = Locadora('Locadaora Sao Joao',9851894151,'Rua daquele lado numero 302', 300,'995421-542')