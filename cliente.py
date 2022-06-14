class Cliente:
    def __init__(self,nome,cpf,dataNascimento,cnh):
        self._nome = nome
        self._cpf = cpf
        self._dataNascimento = dataNascimento
        self._cnh = cnh

    #Caso queira um dado específico do cliente
    def ver_nome(self):
        print("Nome do Cliente:", self._nome)
    def ver_cpf(self):
        print("O Cpf do Cliente eh:", self._cpf)
    def nascimento(self):
        print("Data de nascimento:", self._dataNascimento)
    def numero_cnh(self):
        print("Numero da CNH:", self._cnh)
    
    #Caso queira imprimir todos os dados do cliente com um só comando
    def dados(self):
        print("\nNome do Cliente:", self._nome)
        print("O Cpf do Cliente eh:", self._cpf)
        print("Data de nascimento:", self._dataNascimento)
        print("Numero da CNH:", self._cnh)

cliente1 = Cliente('Pedro','999.999.99-34','18/11/1994','999856565')
cliente2 = Cliente('Felipe','999.999.98-54', '15/10/1999','959595656')