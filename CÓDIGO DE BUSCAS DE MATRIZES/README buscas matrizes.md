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
Como o processo é iniciado pelo primeiro índice, achar o valor logo no começo requer apenas uma única verificação (melhor caso).

b) O que acontece quando o elemento procurado não existe?
É preciso checar todas as posições da estrutura do início ao fim até confirmar de fato a ausência do valor pesquisado.

c) Qual é o pior caso da busca sequencial?
Ocorre quando o item procurado está no último índice ou ausente, obrigando o algoritmo a checar cada uma das posições disponíveis.

d) Como o aumento das dimensões da matriz influencia a quantidade de operações?
O tamanho da estrutura é proporcional às verificações necessárias. Por exemplo, em uma tabela $100 \times 100$, aumentam-se as checagens para até $10.000$ posições.

e) Qual a complexidade da busca sequencial em uma matriz com m linhas e n colunas?
A complexidade é O(m × n), pois, no pior caso, todos os elementos da matriz precisam ser percorridos.
