from time import sleep
from Errors import *

class Tabuleiro:
    def __init__(self, linhas):
        """
            Inicializador de um tabuleiro de sudoku. Seu único atributo é o conjunto de linhas
            preenchidas inicialmente.

            list[list[int]] -> Tabuleiro
        """
        self.linhas = linhas
        self.possibilidades = [[set([1,2,3,4,5,6,7,8,9]) for x in range(9)] for x in range(9)]

    def ChecarConjunto(self, nomeConjunto, numConjunto):
        """
            Checa os números restantes na conjunto indicada por nomeConjunto e numConjunto
            e retorna um conjunto com esses números

            (str, int) -> set
        """
        conjunto = self.GetCojunto(nomeConjunto, numConjunto)
        possibilidadesConjunto = set()

        for x in [1,2,3,4,5,6,7,8,9]:
            if x not in conjunto:
                possibilidadesConjunto.add(x)
        
        return possibilidadesConjunto
        
    def GetCojunto(self, nomeConjunto, numConjunto):
        """
            Retorna o conjunto de tipo especificado e de número especificado
            Tipos aceitos:
            - linha
            - coluna
            - quadrado

            (str, int) -> list[int]
        """
        if nomeConjunto == "linha":
            return self.linhas[numConjunto]

        elif nomeConjunto == "coluna":
            coluna = []
            for i in range(9):
                coluna.append(self.linhas[i][numConjunto])
            return coluna

        elif nomeConjunto == "quadrado":
            quadrado = []
            for i in range(3):
                for j in range(3):
                    quadrado.append(self.linhas[(numConjunto // 3) * 3 + i][(numConjunto % 3) * 3 + j])
            return quadrado
        else:
            raise ConjuntoInexistenteError
    
    def Resolver(self):
        """
            Um algoritmo para resolver o tabuleiro de sudoku armazenado

            None -> None
        """
        while (not self.Ganhou()):
            for i in range(9):
                for j in range(9):
                    if self.linhas[i][j] == 0:
                        #Listar todas as possibilidades
                        quadPossibilides = self.possibilidades[i][j]
                        numQuadrado = (i // 3) * 3 + j // 3
                        quadPossibilides.difference_update(self.GetCojunto("linha", i))
                        quadPossibilides.difference_update(self.GetCojunto("coluna", j))
                        quadPossibilides.difference_update(self.GetCojunto("quadrado", numQuadrado))
                        #Checar para ver se existe possibilidade única
                        if len(quadPossibilides) != 1:
                            self.possibilidades[i][j] = quadPossibilides
                        else:
                            self.linhas[i][j] = quadPossibilides.pop()

    def __str__(self):
        tabuleiro = ""

        for i, linha in enumerate(self.linhas):
            if i % 3 == 0 and i > 0:
                tabuleiro += "- - - + - - - + - - -\n"
            for j, number in enumerate(linha):
                if j % 3 == 0 and j > 0:
                    tabuleiro += "| "
                tabuleiro += [str(number), " "][number == 0] + " "
            tabuleiro += "\n"
        
        return tabuleiro

    def Ganhou(self):
        for x in [1,2,3,4,5,6,7,8,9]:
            for i in range(9):
                conjuntoTotal = self.GetCojunto("linha", i) + self.GetCojunto("coluna", i)
                if conjuntoTotal.count(x) != 2:
                    return False
        return True