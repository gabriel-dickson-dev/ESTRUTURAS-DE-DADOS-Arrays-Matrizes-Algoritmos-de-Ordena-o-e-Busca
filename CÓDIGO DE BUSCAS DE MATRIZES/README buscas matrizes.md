# Busca Sequencial em Matriz


**Implementação de uma busca sequencial em matrizes, analisando a quantidade de operações necessárias para encontrar um elemento no início, no final ou quando ele não existe.**

Resultados
Matriz	Elementos	Início	Final	Inexistente
2 × 2	4	1	4	4
10 × 10	100	1	100	100
100 × 100	10.000	1	10.000	10.000
Análise
---

a) Por que encontrar um elemento no início exige menos operações?
Porque a busca começa pela primeira posição. Se o elemento estiver nela, apenas uma comparação é necessária.

b) O que acontece quando o elemento procurado não existe?
A matriz inteira precisa ser percorrida antes de concluir que o elemento não está presente.

c) Qual é o pior caso da busca sequencial?
Quando o elemento está na última posição ou não existe, sendo necessário verificar todos os elementos do codigo.

d) Como o aumento das dimensões da matriz influencia a quantidade de operações?
Quanto maior a matriz, maior a quantidade de elementos que podem precisar ser comparados. Uma matriz 100 × 100 possui 10.000 elementos.

e) Qual a complexidade da busca sequencial em uma matriz com m linhas e n colunas?
A complexidade é O(m × n), pois, no pior caso, todos os elementos da matriz precisam ser percorridos.
