#algoritmo utilizado para encontrar caminho mais rápido / menor custo. Não pode ser utilizado
# em grafos que possuem arestas negativas.
grafo = {}
grafo["inicio"] = {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2

grafo["a"] ={}
grafo["a"]["fim"] = 1

grafo["b"] ={}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

#vértice final não tem fim
grafo["fim"] = {}

#tabela de custo
infinito = float("inf")
custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

#tabela pais
pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

processados = []

def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo =float("inf")
    nodo_custo_mais_baixo = None
    #percorre cada vertice
    for nodo in custos:
        custo = custos[nodo]
        #executa se custo é menor e nodo não foi processado
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

#encontra o custo mais baixo que ainda não foi processado
nodo = ache_no_custo_mais_baixo(custos)

#caso todos os vertices tenham sido processados este while será encerrado
while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    #percorrer todos os viznhos do vertice
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        #testando se esforço vizinho é mais barato
        if custos[n] > novo_custo:
            #atualiza custo
            custos[n] = novo_custo
            #este vertice se torna o novo pai do vizinho
            pais[n] = nodo
    #marca vertice como processado
    processados.append(nodo)
    #encontra o próximo vertice a ser processado e o algoritmo é processado
    nodo = ache_no_custo_mais_baixo(custos)

print("Custo do inicio até cada nodo:")
print(custos)


