vetmatricula = []

a = 0

for cont in range(5):
    vetmatricula.append(int(input("DIGITE O NÚMERO PARA CADASTRO DE MATRÍCULA:")))

busca = int(input("Informe a matrícula para consulta:"))

for cont in range(5):
    
    if busca == vetmatricula[cont]:
        break
    a=a+1
    
if cont == 5:
    print("\n Matricula não encontrada \n")
    
else:
    print("Encontrado \n")

    
