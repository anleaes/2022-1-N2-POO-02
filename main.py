from cliente import *
from veiculo import *
from funcionario import *
from gerente import *
from vendedor import *
from seguro import *
from locadora import *
from pagamento import *


# E aqui aparece os dados da locadora
locadora1.resumo()
# Cadastro do cliente
cliente1.dados()
print("\n")
# O cliente fala o tipo de carro que ele quer comprar/alugar
veiculo1.especificacoes()
veiculo1.disponivel()
print("\n")

# Ele é atendido pelo vendedor/gerente da loja
gerente1.dados()
print("\n")
# vendedor1.dados()
# Aqui o Funcionario preenche as informações no caixa
pagamento1.modoPagamento()
pagamento1.tipo_transacao()
pagamento1.aluguel()
pagamento1.preco()
pagamento1.parcelamento()
pagamento1.juros()
print("\n")
# Seguro obrigatório
seguro1.contrato()


