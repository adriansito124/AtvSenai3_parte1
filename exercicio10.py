# -> trabalhorenda

func = 0
cod = int(input("QUAL SEU CÓDIGO:\n"))
valorimposto = 0

while cod > 0:
    func=func+1
    qta_dep = int(input("QUANTOS DEPENDENTES VOCÊ TEM: \n"))
    rendamensal = float(input("QUAL SUA RENDA MENSAL: \n"))
    
    rendamensal = round(rendamensal, 2)

    print(f"\nA renda Mensal Informada é de: R$ {rendamensal}")

    if rendamensal <= 1399.12:
        valorinss = rendamensal*0.08
        valorinss = round(valorinss, 2)
        print(f"\nValor do INSS mensal: R$ {valorinss} .")
    else:
        if rendamensal >= 1399.13 and rendamensal <= 2331.88:
            valorinss = rendamensal*0.09
            valorinss = round(valorinss, 2)
            print(f"\nValor do INSS mensal: R$ {valorinss} .")
        else:
            if rendamensal >= 2331.89 and rendamensal < 4663.75:
                valorinss = rendamensal*0.11
                valorinss = round(valorinss, 2)
                print(f"\nValor do INSS mensal: R$ {valorinss} .")
            else:
                if rendamensal >= 4663.75:
                    valorinss = 513.01
                    valorinss = round(valorinss, 2)
                    print(f"\nValor do INSS mensal: R$ {valorinss} .")
                
    valorfinalinss = rendamensal - valorinss

    valorcalculoIR = valorfinalinss - (qta_dep * 189.59)


    if valorcalculoIR <= 1903.98:
        valorfinal = valorfinalinss
        print("\nValor do IR: R$ 0,0 .")
        valorfinal = round(valorfinal, 2)
        print(f"\nSalário liquido sem dedução por dependente: R$ {valorfinal}")
    else:
        if valorcalculoIR >= 1903.99 and valorcalculoIR <=2826.65:
            
            valorimposto = (valorcalculoIR*0.075) - 142.80
            valorimposto = round(valorimposto, 2)
            valorfinal = valorfinalinss - valorimposto
            print(f"\nValor do IR mensal: R$ {valorimposto} .")
            valorfinal = round(valorfinal, 2)
            print(f"\nSalário liquido sem dedução por dependente: R$ {valorfinal}")
        else:
            if valorcalculoIR >= 2826.66 and valorcalculoIR <= 3751.05:
                
                valorimposto = (valorcalculoIR*0.15) - 354.80
                valorimposto = round(valorimposto, 2)
                valorfinal = valorfinalinss - valorimposto
                print(f"\nValor do IR mensal: R$ {valorimposto} .")
                valorfinal = round(valorfinal, 2)
                print(f"\nSalário liquido sem dedução por dependente: R$ {valorfinal}")
            else:
                if valorcalculoIR >= 3751.06 and valorcalculoIR <= 4664.68:
                    
                    valorimposto = (valorcalculoIR*0.225) - 636.13
                    valorimposto = round(valorimposto, 2)
                    valorfinal = valorfinalinss - valorimposto
                    print(f"\nValor do IR mensal: R$ {valorimposto} .")
                    valorfinal = round(valorfinal, 2)
                    print(f"\nSalário liquido sem dedução por dependente: R$ {valorfinal}")
                else:
                    if valorcalculoIR > 4664.68:
                        
                        valorimposto = (valorcalculoIR*0.275) - 869.36;
                        valorimposto = round(valorimposto, 2)
                        valorfinal = valorfinalinss - valorimposto
                        print(f"\nValor do IR mensal: R$ {valorimposto} .")
                        valorfinal = round(valorfinal, 2)
                        print(f"\nSalário liquido sem dedução por dependente: R$ {valorfinal}")

    inssanual = valorinss * 12
    iranual = valorimposto * 12
    inssanual = round(inssanual, 2)
    iranual = round(iranual, 2)
    print(f"\nINSS anual: R$ {inssanual} .\n")
    print(f"IR anual: R$ {iranual} .\n")


    valorfinal = valorfinal - (189.59 * qta_dep)
    print(f"Valor do Salário liquido(com dedução de dependentes): R$ {valorfinal}  \n")


    print(f"\n {func}º funcionário calculado.")

    print("\n\n\n")
    cod = int(input("QUAL SEU CÓDIGO:\n"))





