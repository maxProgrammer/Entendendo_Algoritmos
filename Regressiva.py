def regressiva(i):
    print(i)

    if i <=1:
        return

    else:
        regressiva(i-1)

#testando  funçao regressiva
regressiva(10)
