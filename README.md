# nonlinear-programming

Exercício programa da disciplina MAP2212 - Laboratório de Computação e Simulação, ministrada pelo professor Julio M. Stern do IME-USP no primeiro semestre de 2013

#
O objetivo deste exercício é fazer um programa que implemente:

1. O Algoritmo de busca linear por ajuste quadrático descrito na seção D.3.2 de [1]

2. O Algoritmo ParTan Gradiente em dimensão 'd', descrito na seção D.3.3 de [1], utilizando a sub-rotina de busca linear (1).

3. Escrever um programa utilizando (1) e (2) para encontrar o mínimo irrestrito de uma função f(x).

#
2 Dados de Entrada
Como entrada serão dadas as seguintes informações em um arquivo entrada.py:
- d: variável com a dimensao da função
- f(x): uma função implementando f
- g(x): uma função implementando o gradiente de f
- x0: vetor com o ponto inicial
- eps: variável com a precisão desejada para o ponto de ótimo, x*

#
3 Dados de Saída
O programa gera um arquivo saida.txt contendo na primeira linha o valor ótimo
obtido (f(x*)) e na segunda linha o argumento ótimo (x*)

#
Referências
[1] http://www.ime.usp.br/~jstern/books/evli.pdf

