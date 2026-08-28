# Análise Experimental: Bubble Sort e Quick Sort

***Esta etapa apresenta a análise dos resultados obtidos nos experimentos realizados com os algoritmos Bubble Sort e Quick Sort, considerando diferentes tamanhos de arrays: 10, 20 e 1.000 elementos.***

Resultados e Análise
---

a) Qual algoritmo realizou menos operações para 10 elementos?

Para um array contendo 10 elementos, a diferença entre os algoritmos é relativamente pequena. De acordo com os resultados apresentados na tabela experimental, o Quick Sort tende a realizar menos operações que o Bubble Sort.

b) O comportamento permaneceu igual para 20 elementos?

Não. Com o aumento para 20 elementos, a diferença entre os algoritmos começa a se tornar mais evidente. O Quick Sort tende a apresentar uma quantidade menor de operações, enquanto o número de operações do Bubble Sort cresce de maneira mais significativa.

c) O que aconteceu quando o tamanho aumentou para 1.000 elementos?

Com 1.000 elementos, a diferença entre os algoritmos tornou-se significativamente maior. O Bubble Sort realizou uma quantidade muito superior de operações, enquanto o Quick Sort conseguiu realizar a ordenação utilizando uma quantidade consideravelmente menor de operações.
Esse resultado demonstra como a escolha do algoritmo pode ter grande impacto no desempenho quando o tamanho da estrutura de dados aumenta.

d) Qual algoritmo apresentou maior crescimento na quantidade de operações?

O Bubble Sort apresentou o maior crescimento na quantidade de operações conforme o tamanho do array aumentou. Isso ocorre devido à sua complexidade média e de pior caso ser O(n²).

e) Os resultados experimentais são coerentes com as complexidades teóricas estudadas?

Sim. Os resultados experimentais são coerentes com as complexidades teóricas dos algoritmos.
O Bubble Sort possui complexidade média O(n²), fazendo com que a quantidade de operações cresça rapidamente conforme o número de elementos aumenta.
O Quick Sort, por sua vez, possui complexidade média O(n log n), apresentando um crescimento de operações significativamente menor na maioria dos casos.
Portanto, conforme o tamanho do array aumenta, a vantagem de desempenho do Quick Sort tende a se tornar cada vez mais evidente.

f) Em qual situação seria escolhido o Bubble Sort?

O Bubble Sort seria escolhido principalmente para arrays pequenos ou em situações nas quais a simplicidade de implementação seja mais importante que o desempenho.
Também é um algoritmo adequado para fins didáticos, pois sua lógica de comparação e troca de elementos é simples de compreender e permite estudar conceitos fundamentais de ordenação.

g) Em qual situação seria escolhido o Quick Sort?

O Quick Sort seria escolhido para arrays maiores, principalmente quando é necessário obter um melhor desempenho na ordenação.
Para estruturas com aproximadamente 1.000 elementos ou mais, o Quick Sort tende a ser uma alternativa mais adequada que o Bubble Sort, devido ao seu menor crescimento médio na quantidade de operações.
