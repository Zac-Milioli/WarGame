"""
## Card

Este módulo define a classe `Card` e suas funções
"""
from .war_vars import WarVars

class Card:
    """
    ## Cartas do jogo.

    Contém os seguintes atributos:
    ```
    suit: str (Hearts, Diamonds, ...)

    rank: str (Two, Three, King, Ace, ...)

    value: int (Definido automaticamente)
    ```
    """
    def __init__(self, suit: str, rank: str):
        self.suit: str = suit
        self.rank: str = rank
        self.value: int = WarVars.VALUES[self.rank]

    @property
    def get_suit(self) -> str:
        """
        Retorna o parâmetro suit em formato de string
        ```
        self.suit
        ```
        """
        return self.suit

    @property
    def get_rank(self) -> str:
        """
        Retorna o parâmetro rank em formato de string
        ```
        self.rank
        ```
        """
        return self.rank

    @property
    def get_value(self) -> int:
        """
        Retorna o parâmetro value em formato de int
        ```
        self.value
        ```
        """
        return self.value

    def __str__(self) -> str:
        return f'{self.get_rank} of {self.get_suit}'
