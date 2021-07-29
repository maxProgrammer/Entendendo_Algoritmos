#função que recebe uma lista e item parametrizados
def pesquisaBinaria(lista,item):
    menor = 0
    maior = len(lista)- 1

    #for utilizado para percorrer toda lista
    while menor <= maior:

        # variavel para guardar  posicao meio
        meio = (menor + maior) //2
        
        #variavel para guardar valor posicao meio
        palpite = lista[meio]
        
        #se item for encontrado retorno posicao
        if palpite  == item:
            return meio

        # se palpite for maior que item, maior recebe meio -1
        elif palpite > item:
            maior = meio -1
        #se palpite for menor que item, menor recebe meio + 1
        else:
            menor = meio + 1
            
    # se item não existir na lista retorna None
    return None

lista = [1,3,5,7,9]

print(pesquisaBinaria(lista,9))
print(pesquisaBinaria(lista,0))
    
    
