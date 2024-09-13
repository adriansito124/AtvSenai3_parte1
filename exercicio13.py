matriz = [[],[],[]]

for l in range(3):
    for c in range(5):
        matriz[l].append(int(input(f"Informe a posição {l}, {c} da matriz")))

print("\n")

for l in range(3):
    print(f"{matriz[l]}")
