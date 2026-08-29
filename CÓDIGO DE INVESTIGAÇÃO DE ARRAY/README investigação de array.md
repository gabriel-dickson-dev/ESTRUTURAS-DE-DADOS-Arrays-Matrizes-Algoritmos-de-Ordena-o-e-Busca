# Lista de Temperaturas

Uma lista é utilizada para armazenar as temperaturas, sem a necessidade de definir previamente a quantidade de posições, como ocorre em algumas linguagens.

O comando ***for*** é utilizado para solicitar as 10 temperaturas. O método ***append()*** adiciona cada valor ao final da lista.

Os elementos são acessados por índices, começando pelo índice `0`. Dessa forma, uma lista com 10 temperaturas possui índices de 0 ao 9.

## Operações

Considerando os percursos realizados pelo algoritmo:

* Entrada das 10 temperaturas: 10 operações
* Exibição: 10 operações
* Cálculo da média: 10 operações
* Busca do maior e menor: 9 operações
* Contagem acima da média: 10 operações

**Total aproximado: 49 operações de percurso** para 10 elementos, desconsiderando operações constantes e detalhes internos da linguagem.

## Complexidade

O algoritmo realiza vários percursos sobre a lista. Como cada percurso percorre os elementos uma vez, a complexidade geral é **O(n)**, onde "n" representa a quantidade de temperaturas.
