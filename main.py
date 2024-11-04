"""
## Arquivo principal a ser executado para jogar

Desenvolvido por Zac Milioli
"""
from war import Game

if __name__ == "__main__":
    game = Game(player_1="Bot 1", player_2="Bot 2", war_size=8)
    game.run()
