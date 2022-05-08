class ConjuntoInexistenteError(Exception):
    """
        Erro levantado ao tentar checar algo que não é um conjunto válido
    """

    def __init__(self, nomeConjunto, mensagem = "Conjunto não existe no contexto de Sudoku"):
        self.nomeConjunto = nomeConjunto
        self.mensagem = mensagem
        super().__init__(self.mensagem)

    def __str__(self):
        return f"{self.nomeConjunto} -> {self.mensagem}"