def busca(matriz, valor):
    comparacoes = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            comparacoes += 1

            if matriz[i][j] == valor:
                print(f"Linha: {i}, Coluna: {j}")
                print(f"Comparações: {comparacoes}")
                return comparacoes

    print(f"Valor inexistente. Comparações: {comparacoes}")
    return comparacoes


for n in [2, 10, 100]:
    matriz = [[i * n + j + 1 for j in range(n)] for i in range(n)]

    print(f"\n--- Matriz {n}x{n} ---")

    busca(matriz, 1)        # início
    busca(matriz, n * n)    # final
    busca(matriz, 99999)    # inexistente
