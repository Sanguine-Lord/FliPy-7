from dataclasses import dataclass
from random import *

@dataclass
class GameState:
    player_count: int
    turn_number: int
    target_score: int

#def Setup(self, player_count, target_score)
#   initial_players = {}
#   for i in range(1, player_count + 1):
#       initial_players[f"player_{i}"] = Player()
#       int(player_type) = input("Who is f"Player {i}"? 0 = Human, 1 = CPU")
#       match player_type:
#           case 0:
#               initial_players[f"player_{i}"].type = "Human"
#           case 1:
#               initial_players[f"player_{i}"].type = "CPU"
