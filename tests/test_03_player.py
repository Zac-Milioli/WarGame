"""
Testes para o módulo Player
"""

from war import Player, Card

class TestPlayer:
    """
    Classe para uso do Pytest
    """
    test_card = Card(suit="Test", rank="Two")

    def test_01_create_player(self):
        """
        Testa a criação de um Player
        """
        test_player = Player(name="TestPlayer")
        assert not test_player.get_cards
        assert test_player.get_name == "TestPlayer"

    def test_02_add_card(self):
        """
        Testa a adição de uma carta ao baralho do Player
        """
        test_player = Player(name="TestPlayer")
        test_player.add_card(new_cards=self.test_card)
        assert len(test_player.get_cards) == 1
        test_player.add_card(new_cards=[self.test_card,self.test_card,self.test_card])
        assert len(test_player.get_cards) == 4

    def test_03_remove_card(self):
        """
        Testa a remoção de cartas do baralho do Player
        """
        test_player = Player(name="TestPlayer")
        test_player.add_card(new_cards=[self.test_card,self.test_card,self.test_card])
        first_card = test_player.get_cards[0]
        removed_card = test_player.remove_card()
        assert len(test_player.get_cards) == 2
        assert str(first_card) == str(removed_card)
