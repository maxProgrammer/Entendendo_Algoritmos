#algoritmo  utilizado para pesquisa em uma lista ordenada.
#sua principal vantagem sobre a pesquisa linear é o tempo de execução logaritmo.
#utilizado muito para pesquisa de usuários
def pesquisabinaria(lista, item):
    #inicia posicao inicial como indice zero
    menor  = 0
    #inicia posicao final como final da lista
    maior = len(lista) -1

    #procura item enquanto não chegar no final da lista
    while menor <= maior:
        #encontra o meio da lista
        meio = (menor + maior) // 2
        #armazena o valor do meio da lista na variavel
        palpite = lista[meio]

        #se item esta no meio da lista e retorna a posicao que o programa esta inserido
        if palpite == item:
            return "{} está na posicao {}.".format(item,meio)
            break
        #se meio da lista e maior do que item informado posicao final da lista será o meio atual - 1
        elif palpite > item:
            maior = meio - 1
        # se meio da lista e menor do que item informado inicio sera meio da lista mais + 1
        else:
            menor = meio + 1
    #se numero nao é encontrado retorna que o item não está na lista
    return "{} não está na lista.".format(item)

#testa o programa
lista = [1,3,5,7,9]
print(pesquisabinaria(lista,7))
print(pesquisabinaria(lista,-4))

                
