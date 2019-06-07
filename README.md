# nonlinear-programming

Programa desenvolvido na disciplina MAP2212 - Laboratório de Computação e Simulação, ministrada pelo professor Julio M. Stern do IME-USP no primeiro semestre de 2013

#
No programa está implementado:

1. O Algoritmo de busca linear por ajuste quadrático descrito na seção D.3.2 de [1]

2. O Algoritmo ParTan Gradiente em dimensão 'd', descrito na seção D.3.3 de [1], utilizando a sub-rotina de busca linear (1).

3. Um algoritmo utilizando (1) e (2) para encontrar o mínimo irrestrito de uma função f(x).

#
Dados de Entrada:

Como entrada serão dadas as seguintes informações em um arquivo entrada.py:
- d: variável com a dimensao da função
- f(x): uma função implementando f
- g(x): uma função implementando o gradiente de f
- x0: vetor com o ponto inicial
- eps: variável com a precisão desejada para o ponto de ótimo, x*

#
Dados de Saída:

O programa gera um arquivo saida.txt contendo na primeira linha o valor ótimo
obtido (f(x*)) e na segunda linha o argumento ótimo (x*)

#
Referências
[1] http://www.ime.usp.br/~jstern/books/evli.pdf

