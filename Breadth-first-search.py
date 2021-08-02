from collections import deque

def pessoa_e_vendedor(nome):
    return nome[-1] == 'm'

grafo = {}
grafo["max"] = ["alice","bob","claire"]
grafo["bob"] = ["anuj","peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"]=["thom","jonny"]
grafo["anuj"]=[]
grafo["peggy"]=[]
grafo["thom"]=[]
grafo["jonny"]=[]

def pesquisa(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    #vetor responsável pelo registro das pessoas já verificadas
    verificadas = []
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        #verifica a pessoa se ela ainda não está na lista das verificadas
        if pessoa not in verificadas:
            if pessoa_e_vendedor(pessoa):
                print (pessoa + " é um vendedor de manga!")
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                #adiciona a pessoa na lista das verificadas
                verificadas.append(pessoa)

    return False

pesquisa("max")


