"""
## Deck

Este módulo define a classe `Deck` e suas funções
"""
from random import shuffle
from .war_vars import WarVars
from .card import Card

class Deck:
    """
    ## Baralho de cartas.

    Contém os seguintes atributos:
    ```
    cards: list
    ```
    """
    def __init__(self):
        self.cards: list = []
        for suit in WarVars.SUITS:
            for rank in WarVars.RANKS:
                self.cards.append(Card(suit=suit, rank=rank))

    @property
    def get_cards(self) -> list:
        """
        Retorna a lista de cartas do baralho, em formato das strings
        em `__repr__`
        ```
        self.value
        ```
        """
        cards_list = []
        for card in self.cards:
            cards_list.append(f"{card}")
        return cards_list

    def shuffle_deck(self) -> None:
        """
        Embaralha as cartas do baralho.
        """
        shuffle(self.cards)

    def deal_one(self) -> Card:
        """
        Entrega a última carta do Deck para o jogador
        """
        return self.cards.pop()

    def __str__(self):
        return f"Deck of cards with: {', '.join(self.get_cards)}"
