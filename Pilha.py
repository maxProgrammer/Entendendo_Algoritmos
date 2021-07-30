def sauda2(nome):
    print ("Como  vai " + nome + "?")

def tchau():
    print("Ok. Tchau!")

def sauda(nome):
    print("Olá, " + nome + "!")
    sauda2(nome)
    print("preparando para dizer tchau...")
    tchau()

#testando pilha
sauda("Max")
