from asyncio.windows_events import NULL


class Pagamento:
    def __init__(self, modoPagamento,tipoTransacao,aluguel,preco,parcelado, valorAdicional):
        self._modoPagamento = modoPagamento
        self._tipoTransacao = tipoTransacao
        self._aluguel = aluguel
        self._preco = preco
        self._valorAdicional = valorAdicional
        self._parcelado = parcelado

    def modoPagamento(self):
            if self._modoPagamento == 'Cheque':
                print('Metodo invalido')
            else:
                print(self._modoPagamento)
    
    def tipo_transacao(self):
        print ("Tipo de transacao:", self._tipoTransacao)
    
    def aluguel(self):
        print("Valor dor aluguel:", self._aluguel)
    
    def preco(self):
        print("Valor de venda do carro",self._preco)

    def parcelamento(self):
        print("Voce pode parcelar em ate 20 vezes")
        vezes = input()
        
        if vezes > 1:
            print("Numero de vezes do parcelamento eh: " , + vezes)
        else:
            print("Pagamento a vista")

    def juros(self):
        print("Compras parceladas tem um juros de:", self._valorAdicional)

pagamento1 = Pagamento('Cartao','Compra',NULL,30000.99,'10x',3000)
pagamento2 = Pagamento('Cheque',NULL,NULL,NULL,NULL,NULL)
