#algoritmo utilizado pesquisar, evitar lançamentos duplicados e aplicação de cache para melhorar tempo de carregamento da página.
# 
voted = {}
def verifica_eleitor(nome):
    #funcao get retorna valor do dicionario
    if voted.get(nome):
        print("Voto já realizado")

    else:
        voted[nome] = True
        print ("Votação liberada")

#teste
verifica_eleitor("tom")
verifica_eleitor("max")
verifica_eleitor("max")
verifica_eleitor("Tom")
