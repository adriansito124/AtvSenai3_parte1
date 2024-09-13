vetor1 = []
vetor2 = []
prod = 0

print("Entre com um vetor de 5 elementos\n")
for i in range(5):
    vetor1.append(int(input(f"Elemento {i+1}:")))

print(f"Entre com um outro vetor de {len(vetor1)} elementos\n")
for i in range(5):
     vetor2.append(int(input(f"Elemento {i+1}:")))

for i in range(5):
    prod = prod + vetor1[i] * vetor2[i]

print(f"O produto vale {prod}")

