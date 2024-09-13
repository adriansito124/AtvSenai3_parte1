tempo = int(input("INFORME O TEMPO DE FIDELIDADE:"))
valor = int(input("INFORME O VALOR GASTO NA COMPRA :"))

if tempo >= 5:
    if valor > 5000:
        print("20%\n")
    else:
        if valor > 1000:
            print("10%\n")
        else:
            print("SEM DESCONTO")
else:
    print("SEM DESCONTO")

