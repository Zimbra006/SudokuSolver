"""
    A ideia deste projeto é criar um algoritmo que resolva qualquer tabuleiro de sudoku

    Sudoku é um jogo composto de 9 linhas e 9 colunas, onde os números de 1 a 9 estão escritos de forma única.
    Além disso, existem 9 quadrados 3 x 3 com a mesma propriedade.

    O objetivo do jogador, e do algoritmo, é encontrar a disposição correta dos números no tabuleiro.

    0 4 2 | 5 0 0 | 0 9 8
    0 0 0 | 2 4 7 | 0 1 0
    7 0 1 | 0 0 0 | 5 0 2
    - - - + - - - + - - -
    8 0 0 | 9 7 0 | 4 0 6
    1 7 6 | 0 0 0 | 8 0 9
    9 5 0 | 0 2 8 | 0 0 1
    - - - + - - - + - - -
    6 1 9 | 4 8 0 | 0 3 7
    0 0 7 | 1 0 2 | 9 8 5
    0 0 5 | 0 9 3 | 0 0 0

    Exemplo de tabuleiro de sudoku não resolvido. Os 0's são representativos de espaços vazios.

    As linhas, colunas e quadrados são numerados de 0 a 8 internamente.
    As linhas começam crescem de cima para baixo.
    As colunas, da esquerda para a direita.
    Os quadrados, da seguinte forma:

    0 | 1 | 2
    - + - + -
    3 | 4 | 5
    - + - + -
    6 | 7 | 8

"""
from Tabuleiro import *
from Tests import *

tab = Tabuleiro(TABULEIRO_MEDIO)
tab.Resolver()
print(tab)