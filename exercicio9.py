#-> sistematabuadas.c

print("_____________________________________________________\n")
print("SISTEMA DE TABUADA \n")
print("_____________________________________________________\n")
num = int(input("digite o número da tabuada que gostaria de consultar: \n"))
print(f"{num} foi o número digitado.\n")

while(num <99):

    match num:
        case 0:
            for i in range(11):
                resp = num*i
                print(f"{num} X {i} = {resp} \n")           
        case 1:
            for i in range(11):
                resp = num*i
                print(f"{num} X {i} = {resp} \n")
        case 2:
            for i in range(11):
                resp = num*i
                print(f"{num} X {i} = {resp} \n")
        case 3:
            for i in range(11):
                resp = num*i
                print(f"{num} X {i} = {resp} \n")
        case 4:
            for i in range(11):
                resp = num*i
                print(f"{num} X {i} = {resp} \n")
        case 5:
            for i in range(11):
                resp = num*i
                print(f"{num} X {i} = {resp} \n")
        case 6:
            for i in range(11):
                resp = num*i
                print(f"{num} X {i} = {resp} \n")
        case 7:
            for i in range(11):
                resp = num*i
                print(f"{num} X {i} = {resp} \n")
        case 8:
            for i in range(11):
                resp = num*i
                print(f"{num} X {i} = {resp} \n")
        case 9:
            for i in range(11):
                resp = num*i
                print(f"{num} X {i} = {resp} \n")
        case 10:
            for i in range(11):
                resp = num*i
                print(f"{num} X {i} = {resp} \n")
        case _:
            print("_____Digite um número de 0 a 10_____ \n\n\n")     
                  
            
    print("Digite o número da tabuada que gostaria de consultar, \n")
    num = int(input("Ou pressione 99 para sair. \n\n"))
    print(f"{num} foi o número digitado.\n")


