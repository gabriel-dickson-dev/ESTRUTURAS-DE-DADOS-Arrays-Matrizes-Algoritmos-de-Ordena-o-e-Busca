temperaturas = []

# 1. Receber as 10 temperaturas
for i in range(10):
    temperatura = float(input(f"Digite a temperatura {i}: "))
    temperaturas.append(temperatura)

# 2. Mostrar todos os elementos
print("\nTemperaturas armazenadas:")
for i in range(10):
    print(f"Índice {i}: {temperaturas[i]}")

# 3. Calcular a média
soma = 0

for temperatura in temperaturas:
    soma += temperatura

media = soma / 10

# 4 e 5. Identificar maior e menor valor
maior = temperaturas[0]
menor = temperaturas[0]

# 6 e 7. Identificar os índices
indice_maior = 0
indice_menor = 0

for i in range(1, 10):
    if temperaturas[i] > maior:
        maior = temperaturas[i]
        indice_maior = i

    if temperaturas[i] < menor:
        menor = temperaturas[i]
        indice_menor = i

# 8. Contar valores acima da média
acima_media = 0

for temperatura in temperaturas:
    if temperatura > media:
        acima_media += 1

# Resultados
print(f"\nMédia: {media:.2f}")
print(f"Maior temperatura: {maior:.2f}")
print(f"Índice do maior valor: {indice_maior}")
print(f"Menor temperatura: {menor:.2f}")
print(f"Índice do menor valor: {indice_menor}")
print(f"Valores acima da média: {acima_media}")
