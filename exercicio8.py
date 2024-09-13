idade = int(input("QUAL A IDADE: \n"))
sexo = input("QUAL O SEXO, (M) PARA MASCULINO OU (F) PARA FEMININO: \n")

sexo = sexo.upper()

if sexo == 'M':
    if idade >= 16:
        print("você tem direito a compra de ingressos \n")
    else:
        print("você não pode comprar ingressos \n")
else:
    if idade >= 18:
        print("você tem direito a compra de ingressos \n")
    else:
        print("você não pode comprar ingressos \n")
