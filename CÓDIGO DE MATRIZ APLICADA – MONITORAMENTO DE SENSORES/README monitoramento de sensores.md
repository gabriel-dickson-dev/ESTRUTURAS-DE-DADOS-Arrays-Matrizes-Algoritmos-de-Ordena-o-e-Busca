# Matriz de Sensores

O programa feito em 'c' utiliza uma matriz bidimensional para armazenar as temperaturas registradas por 5 sensores durante 24 horas. Cada linha representa um sensor e cada coluna representa uma hora do dia.

## Estrutura da Matriz

A matriz utilizada possui 5 linhas e 24 colunas, totalizando 120 posições:

5 × 24 = 120

Os índices [i][j] são utilizados para acessar cada posição da matriz. O índice i representa o sensor, variando de 0 a 4, enquanto j representa a hora, variando de 0 a 23.

Percurso da Matriz

Para acessar todos os valores da matriz são utilizados loops aninhados por ser bidimensional. O primeiro loop percorre os sensores e o segundo percorre as 24 horas de cada sensor.

Durante o processamento, são realizadas operações para calcular a média de cada sensor no sistema, a média geral das temperaturas identifica a maior temperatura registrada e contar as medições que estão acima de um limite definido pelo usuário.

Complexidade

O percurso completo da matriz possui 120 posições. Para uma matriz com N linhas e M colunas, a complexidade de tempo do percurso é:

O(N × M)

No caso utilizado no programa:

O(5 × 24)

Como as dimensões da matriz são fixas, o programa realiza uma quantidade determinada de operações para percorrer os dados.

***Resultado***
---

O programa apresenta as médias individuais dos sensores, a média geral do sistema, a maior temperatura registrada com sua localização e a quantidade de temperaturas que ultrapassaram o limite informado.
