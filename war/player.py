"""
## Player

Este módulo define a classe `Player` e suas funções
"""
from .card import Card

class Player:
    """
    ## Jogador

    Contém os seguintes atributos:
    ```
    cards: list
    ```
    """
    def __init__(self, name: str):
        self.name: str = name
        self.cards: list = []

    @property
    def get_cards(self) -> list:
        """
        Retorna as cartas que o jogador possui
        """
        return self.cards

    @property
    def get_name(self) -> list:
        """
        Retorna o nome do jogador
        """
        return self.name

    def add_card(self, new_cards: Card | list[Card]) -> None:
        """
        Adiciona uma ou mais cartas no final do baralho do jogador
        """
        if isinstance(new_cards, list):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)

    def remove_card(self) -> Card:
        """
        Remove a primeira carta do baralho do usuário
        """
        return self.cards.pop(0)

    def __str__(self) -> str:
        return f'{self.name} possui {len(self.cards)} cartas'
