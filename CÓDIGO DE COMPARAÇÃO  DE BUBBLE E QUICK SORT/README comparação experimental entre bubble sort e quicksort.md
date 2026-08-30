# Análise Experimental: Bubble Sort e Quick Sort

***Esta etapa apresenta a análise dos resultados obtidos nos experimentos realizados com os algoritmos Bubble Sort e Quick Sort, considerando diferentes tamanhos de arrays: 10, 20 e 1.000 elementos.***

Resultados e Análise
---

a) Qual algoritmo realizou menos operações para 10 elementos?

O Quick Sort efetuou menos passos computacionais do que o Bubble Sort, embora para 10 itens essa margem de diferença ainda seja bastante sutil.

b) O comportamento permaneceu igual para 20 elementos?

Não. Com o aumento para 20 itens, a discrepância de eficiência ficou mais clara: o Quick Sort manteve um volume menor de passos, enquanto o Bubble Sort teve um salto perceptível no esforço necessário.

c) O que aconteceu quando o tamanho aumentou para 1.000 elementos?

A distância de desempenho entre eles disparou. O Bubble Sort exigiu um número muito mais expressivo de operações, ao passo que o Quick Sort resolveu a ordenação de forma bem mais otimizada, provando o impacto crucial da escolha do algoritmo em bases de dados maiores.

d) Qual algoritmo apresentou maior crescimento na quantidade de operações?

O Bubble Sort apresentou o maior crescimento na quantidade de operações conforme o tamanho do array aumentou. Isso ocorre devido à sua complexidade média e de pior caso ser O(n²).

e) Os resultados experimentais são coerentes com as complexidades teóricas estudadas?

Sim. Os resultados experimentais são coerentes com as complexidades teóricas dos algoritmos.
O Bubble Sort possui complexidade média O(n²), fazendo com que a quantidade de operações cresça rapidamente conforme o número de elementos aumenta.
O Quick Sort, por sua vez, possui complexidade média O(n log n), apresentando um crescimento de operações significativamente menor na maioria dos casos.
Portanto, conforme o tamanho do array aumenta, a vantagem de desempenho do Quick Sort tende a se tornar cada vez mais evidente.

f) Em qual situação seria escolhido o Bubble Sort?

Ele é indicado em cenários com volumes reduzidos de dados, quando a simplicidade do código prioriza sobre a velocidade, ou em contextos educacionais para facilitar o entendimento dos fundamentos de troca e ordenação.

g) Em qual situação seria escolhido o Quick Sort?

O Quick Sort é a melhor opção para manipular grandes volumes de dados, sobretudo quando alta performance na ordenação é um requisito essencial. Em conjuntos de dados na casa dos 1.000 elementos ou superiores, ele se mostra bem superior ao Bubble Sort por apresentar uma taxa de crescimento de operações muito menor.
