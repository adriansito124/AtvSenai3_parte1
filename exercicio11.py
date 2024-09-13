# -> dadosvetor2vetor.c

vetjogo = [0]*20
vetdado = [0]*6

vetdado[0] = 0
vetdado[1] = 0
vetdado[2] = 0
vetdado[3] = 0
vetdado[4] = 0
vetdado[5] = 0

for cont in range(20):
    vetjogo[cont] = int(input("Informe o número tirado no dado(de 1 a 6):"))
    
for cont in range(20):
    vetdado[vetjogo[cont] - 1] = vetdado[vetjogo[cont] - 1] + 1

for cont in range(6):
    print(f"dado[{cont+1}] = {vetdado[cont]}\n")
