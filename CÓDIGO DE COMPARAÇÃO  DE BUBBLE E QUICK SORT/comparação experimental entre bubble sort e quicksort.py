import random

# Bubble Sort
def bubble_sort(lista):
    comparacoes = 0
    trocas = 0
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            comparacoes += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1

    return comparacoes, trocas
# Quick Sort
def quick_sort(lista):
    comparacoes = 0
    movimentacoes = 0
    def ordenar(inicio, fim):
        nonlocal comparacoes, movimentacoes
        if inicio >= fim:
            return
        pivo = lista[fim]
        i = inicio - 1
        for j in range(inicio, fim):
            comparacoes += 1
            if lista[j] <= pivo:
                i += 1
                if i != j:
                    lista[i], lista[j] = lista[j], lista[i]
                    movimentacoes += 1
        if i + 1 != fim:
            lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
            movimentacoes += 1
        ordenar(inicio, i)
        ordenar(i + 2, fim)
    ordenar(0, len(lista) - 1)

    return comparacoes, movimentacoes

random.seed(42)
for tamanho in [10, 20, 1000]:
    original = [
        random.randint(1, 1000)
        for _ in range(tamanho)
    ]
    lista_bubble = original.copy()
    lista_quick = original.copy()
    # Executa os algoritmos
    bubble_comp, bubble_trocas = bubble_sort(lista_bubble)
    quick_comp, quick_mov = quick_sort(lista_quick)

    print("\nTamanho:", tamanho)
    print("Bubble Sort:")
    print("Comparações:", bubble_comp)
    print("Trocas:", bubble_trocas)
    print("Quick Sort:")
    print("Comparações:", quick_comp)
    print("Movimentações:", quick_mov)
