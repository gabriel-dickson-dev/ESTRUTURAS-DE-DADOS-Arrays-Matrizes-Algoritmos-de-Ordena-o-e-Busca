def busca(matriz, valor):
    comparacoes = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            comparacoes += 1
            if matriz[i][j] == valor:
                print(f"Encontrado: linha {i}, coluna {j}")
                print(f"Comparações: {comparacoes}\n")
                return
    print("Valor não encontrado")
    print(f"Comparações: {comparacoes}\n")
# Matrizes
for n in [2, 10, 100]:
    matriz = [[i * n + j + 1 for j in range(n)] for i in range(n)]
    print(f"--- Matriz {n}x{n} ---")
    busca(matriz, 1)           # início
    busca(matriz, n*n - 1)     # próximo ao final
    busca(matriz, 99999)       # inexistente
