class Cliente:
    def __init__(self,nome,cpf,dataNascimento,cnh):
        self._nome = nome
        self._cpf = cpf
        self._dataNascimento = dataNascimento
        self._cnh = cnh

    def ver_nome(self):
        print("Nome do Cliente: ", self._nome)

cliente1 = Cliente('Pedro','999.999.99-34','18/11/1994','999856565')
cliente2 = Cliente('Felipe','999.999.98-54', '15/10/1999','959595656')