valor = float(input("QUAL O VALOR INICIAL: "))
debito = float(input("QUAL OS DÉBITOS: "))
credito = float(input("QUAL OS CRÉDITOS: "))

resp = valor + credito
resp = resp - debito

resp = round(resp, 2)

if resp > 0:
    print(f"Saldo Positivo em R$ {resp}")
else:
    if resp<0:
        print(f"Saldo Negativo em R$ {resp}")
    else:
        print("Saldo Zero")
