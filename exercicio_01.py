
# Exercício 01 - Revisão Métodos e Listas #

###########################################
Menu = '''
+--------------------------------------------+
|Menu                                        |
+--------------------------------------------+
|    1-	Inserir novo produto                 |
|    2-	Relatório de produtos                |
|    3-	Excluir produto                      |
|    4-	Encerrar programa                    |
+--------------------------------------------+
Escolha uma opção: '''


listadeProdutos = ['Camiseta House of Tiamat', 'Trilogia de Livros Tolkien', 'Puzzle Skyline']
listadePreco = [ 79.95, 190.99,  89.84]
listadeQuantidade = [21, 5, 19]


def inserirNovoProduto():
    nomeDoProduto = str(input('Digite o nome do produto: ')).lower()
    return listadeProdutos.append(nomeDoProduto)


def inserirPrecoDoProduto():
    precoDoProduto = float(input('Digite o preço do produto: '))
    return listadePreco.append(precoDoProduto)


def inserirQuantidadeDeProduto():
    qtdeProduto = int(input('Digite a quantidade do produto: '))
    return listadeQuantidade.append(qtdeProduto)


def relatorioProdutos():
    for ind, produto in enumerate(listadeProdutos):
        print(produto)

### OPÇÃO 1
def cadastrarNovoProduto():
    inserirNovoProduto()
    inserirPrecoDoProduto()
    inserirQuantidadeDeProduto()

### OPÇÃO 2
def imprimirProdutos():
    print("___________________ Lista de produtos _____________________")
    print("Produto                          Preço            Quantidade")
    print("___________________________________________________________")

    for ind, produto in enumerate(listadeProdutos):
        print("{0}{1}{2}"
            .format(
            str(produto).ljust(28),
            str(listadePreco[ind]).center(15),
            str(listadeQuantidade[ind]).center(23),
        )
        )
    print ('_' * 60)
    input(' [Enter] Continua...')

### OPÇÃO 3
def excluirProduto():
    relatorioProdutos()
    produto = str(input('Digite o nome do produto que deseja excluir: ')).lower()
    if produto in listadeProdutos:
        p = listadeProdutos.index(produto)
        listadeProdutos.pop(p)
        listadePreco.pop(p)
        listadeQuantidade.pop(p)
        input('O produto foi removido da lista com sucesso! Pressione [Enter] para sair.')
    else:
        input('O produto informado não consta na lista. Pressione [Enter] para sair.')
    input(' [Enter] Continua...')

### Principal 
escolha = 0
while True:
    escolha = input(Menu)
    if escolha == '1':
        cadastrarNovoProduto()
    elif escolha == '2':
        imprimirProdutos()
    elif escolha == '3':
        excluirProduto()
    elif escolha == '4':
        break
    else:
        input('Opção inválida! [Enter]')