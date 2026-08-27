temperaturas = []
for i in range(10):
    temperatura = float(input(f"Digite a temperatura {i}: "))
    temperaturas.append(temperatura)
print("\nTemperaturas armazenadas:")
for i in range(10):
    print(f"Índice {i}: {temperaturas[i]}")
soma = 0
for temperatura in temperaturas:
   soma += temperatura
media = soma / 10
maior = temperaturas[0]
menor = temperaturas[0]
indice_maior = 0
indice_menor = 0
for i in range(1, 10):
    if temperaturas[i] > maior:
        maior = temperaturas[i]
        indice_maior = i
    if temperaturas[i] < menor:
        menor = temperaturas[i]
        indice_menor = i
acima_media = 0
for temperatura in temperaturas:
    if temperatura > media:
        acima_media += 1
print(f"\nMédia: {media:.2f}")
print(f"Maior temperatura: {maior:.2f}")
print(f"Índice do maior valor: {indice_maior}")
print(f"Menor temperatura: {menor:.2f}")
print(f"Índice do menor valor: {indice_menor}")
print(f"Valores acima da média: {acima_media}")
