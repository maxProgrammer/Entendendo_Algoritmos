#algoritmo de ordenação que utilizada a técnica dividir para consquistar.
#quebra o problema em pequenos problemas.
#escolher um pivo e coloca os  menos a esquerda e os maiores a direita
#execute o quicksort recursivamente nos subarrays da esquerda(menores) e direita(maiores)
def quicksort(array):
    #caso base
    if len(array) < 2:
        return array

    #caso recursivo
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)

#teste funcao
print (quicksort([10,5,2,3]))
    
