"""
Testes para o módulo Card
"""

from war import Card, WarVars

class TestCard:
    """
    Classe para uso do Pytest
    """
    def test_01_create_card(self):
        """
        Testa a criação de um Card
        """
        test_card = Card(suit=WarVars.SUITS[0], rank=WarVars.RANKS[0])
        assert test_card.get_suit == WarVars.SUITS[0]
        assert test_card.get_rank == WarVars.RANKS[0]
        assert test_card.get_value == WarVars.VALUES[WarVars.RANKS[0]]

    def test_02_create__high_value_card(self):
        """
        Testa a criação de um Card com valor mais alto 
        """
        test_card = Card(suit=WarVars.SUITS[-1], rank=WarVars.RANKS[-1])
        assert test_card.get_suit == WarVars.SUITS[-1]
        assert test_card.get_rank == WarVars.RANKS[-1]
        assert test_card.get_value == WarVars.VALUES[WarVars.RANKS[-1]]
