class Pagamento:
    def __init__(self, modoPagamento,preco,valorAdicional,parcelado):
        self._modoPagamento = modoPagamento
        self._preco = preco
        self._valorAdicional = valorAdicional
        self._parcelado = parcelado

    def parcelamento(self):
        print("Voce pode parcelar em ate 20 vezes")
        vezes = input()
        print("Numero de vezes do parcelamento eh: " , + vezes)