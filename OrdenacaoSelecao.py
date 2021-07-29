#função que identifica o menor item de uma lista e retorna sua posicao
def encontraMenor(lista):
    #armazena o valor do indice 0 a variavel
    menorValor = lista[0]

    #considera que index zero tem o menor valor
    menorIndex = 0

    #percorre lista do indice 1 ao ultimo
    for i in range(1,len(lista) - 1):

        #compra se lista[i] é menor que menor valor e
        #se verdadeiro atualiza menorValor e menorIndex
        if lista[i] < menorValor:
            menorValor = lista[i]
            menorIndex = i

    #retorna o index do menor valor encontrado
    return menorIndex

#funcao que utiliza a funcaencontra menor
#para gerar outra lista ordenada
def ordenaSelecao(lista):

    #lista que receberá itens ordenados
    ordLista = []

    #percorre todos elementos da lista
    for x in range(len(lista)):

        # a cada iteracao encontra menor item e o insere
        # na nova lista. Funcao pop armazena o item na nova lista
        # e apaga na antiga ao mesmo tempo.
        menor = encontraMenor(lista)
        ordLista.append(lista.pop(menor))

    #retorna nova lista ordenada
    return ordLista

#teste programa    
lista = [3,1,13,5,0,100]
print(ordenaSelecao(lista))
    
