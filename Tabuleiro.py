from Errors import *

class Tabuleiro:
    def __init__(self, linhas: list):
        """
            Inicializador de um tabuleiro de sudoku. Seu único atributo é o conjunto de linhas
            preenchidas inicialmente.

            list[list[int]] -> Tabuleiro
        """
        self.linhas = linhas
        self.possibilidades = [[set([1,2,3,4,5,6,7,8,9]) for x in range(9)] for x in range(9)]

        for i in range(9):
            for j in range(9):
                if self.linhas[i][j] == 0:
                    #Listar todas as possibilidades para cada espaço vazio
                    numQuadrado = (i // 3) * 3 + j // 3
                    self.possibilidades[i][j].difference_update(self.GetCojunto("linha", i))
                    self.possibilidades[i][j].difference_update(self.GetCojunto("coluna", j))
                    self.possibilidades[i][j].difference_update(self.GetCojunto("quadrado", numQuadrado))

    def UpdatePossibilidades(self, nomeConjunto: str, numConjunto: int, numNovo: int):
        """
            Atualiza as possibilidades no conjunto indicado por nomeConjunto e numConjunto,
            retirando os valores iguais a numNovo

            (str, int, int) -> None
        """
        numNovoSet = {numNovo}
        for i in range(9):
            if nomeConjunto == "linha":
                self.possibilidades[numConjunto][i].difference_update(numNovoSet)
            
            elif nomeConjunto == "coluna":
                self.possibilidades[i][numConjunto].difference_update(numNovoSet)
            
            elif nomeConjunto == "quadrado":
                self.possibilidades[(numConjunto // 3) * 3 + i // 3][(numConjunto % 3) * 3 + i % 3].difference_update(numNovoSet)

        
        
    def GetCojunto(self, nomeConjunto: str, numConjunto: int):
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
                        quadPossibilidades = self.possibilidades[i][j]
                        
                        #Checar para ver se existe possibilidade única
                        if len(quadPossibilidades) == 1:
                            numNovo = quadPossibilidades.pop()
                            self.linhas[i][j] = numNovo
                            #Atualizar a linha, coluna e quadrado desse espaço
                            self.UpdatePossibilidades("linha", i, numNovo)
                            self.UpdatePossibilidades("coluna", j, numNovo)
                            self.UpdatePossibilidades("quadrado", (i // 3) * 3 + j // 3, numNovo)

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