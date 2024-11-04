"""
## Game

Este módulo permite instanciar um jogo e executá-lo
"""
from .player import Player
from .deck import Deck

class Game:
    """
    Classe onde ocorre o jogo
    """
    def __init__(self, player_1: str, player_2: str, war_size: int):
        self.player_1 = player_1
        self.player_2 = player_2
        self.war_size = war_size

    def run(self):
        """
        Função principal para iniciar o jogo
        """
        # Instância dos Bots
        bot1 = Player(self.player_1)
        bot2 = Player(self.player_2)

        # Criação e embaralhamento do baralho
        deck = Deck()
        deck.shuffle_deck()

        # Distribuição de cartas
        half_deck = len(deck.get_cards)//2
        for _ in range(half_deck):
            bot1.add_card(deck.deal_one())
            bot2.add_card(deck.deal_one())

        # Início do jogo
        finished = False
        rounds = 0
        winner = "Sem vencedor ainda"
        war_size = self.war_size
        while not finished:
            rounds += 1
            print("- "*40)
            print(f"Rodada {rounds}\n")
            print(f"\nJogador 1\n\tNome: {bot1.get_name}\n\tCartas: {len(bot1.get_cards)}")
            print(f"\nJogador 2\n\tNome: {bot2.get_name}\n\tCartas: {len(bot2.get_cards)}")

            if len(bot1.get_cards) == 0:
                winner = bot2
                finished = True
                break
            if len(bot2.get_cards) == 0:
                winner = bot1
                finished = True
                break

            # Início da rodada
            cards_bot1 = []
            cards_bot2 = []

            cards_bot1.append(bot1.remove_card())
            cards_bot2.append(bot2.remove_card())

            war_on = True
            print("\nResumo:")
            while war_on:
                print(f"\t-> {bot1.get_name} joga {cards_bot1[-1]} ({cards_bot1[-1].value})")
                print(f"\t-> {bot2.get_name} joga {cards_bot2[-1]} ({cards_bot2[-1].value})")
                if cards_bot1[-1].get_value > cards_bot2[-1].get_value:
                    print(f"\n\t{bot1.get_name} venceu este round e recebe",
                            f"{len(cards_bot1) + len(cards_bot2)} cartas!")
                    bot1.add_card(cards_bot1)
                    bot1.add_card(cards_bot2)
                    war_on = False
                elif cards_bot1[-1].get_value < cards_bot2[-1].get_value:
                    print(f"\n\t{bot2.get_name} venceu este round e recebe",
                            f"{len(cards_bot1) + len(cards_bot2)} cartas!")
                    bot2.add_card(cards_bot1)
                    bot2.add_card(cards_bot2)
                    war_on = False
                else:
                    print("\n\tGuerra ativa")
                    if len(bot1.get_cards) < war_size:
                        print(f"\n\t{bot1.get_name} não pode declarar guerra.",
                                f"{bot2.get_name} Venceu.")
                        winner = bot2
                        finished = True
                        break
                    if len(bot2.get_cards) < war_size:
                        print(f"\n\t{bot2.get_name} não pode declarar guerra.",
                                f"{bot1.get_name} Venceu.")
                        winner = bot1
                        finished = True
                        break
                    for _ in range(war_size):
                        cards_bot1.append(bot1.remove_card())
                        cards_bot2.append(bot2.remove_card())

        print("- "*40)
        print(f"""
        Jogo encerrado!

        Vencedor: {winner.get_name}

        N° de Cartas: {len(winner.get_cards)}

        Rodadas: {rounds}

        """)
        return True
