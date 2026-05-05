from dataclasses import dataclass, field
from random import *
from player import *
from deck import *
from UiManager import *

@dataclass
class GameState:
    player_count: int
    round_number: int
    target_score: int
    game_deck: Deck
    player_list: dict = field(default_factory=dict)
    ui: UI

    def setup(self):
        player_type = 0
        self.target_score = self.ui.int_prompt("What is the score you would like to play to? Default game is 200 points")
        self.player_count = self.ui.int_prompt("How many players are there?")
        for i in range(1, self.player_count + 1):
            player_type = self.ui.int_prompt(f"What type of player is player_{i}? 0 = human, 1 = CPU")
            match player_type:
                case 0:
                    self.player_list[f"player_{i}"] = Human_Player(score=0, round_active=True, player_name=f"player_{i}")
                case 1:
                    self.player_list[f"player_{i}"] = CPU_Player(score=0, round_active=True, player_name=f"player_{i}")
        self.game_deck.create_deck()

    def victory_check(self):
        for player in self.player_list.values():
            if player.score >= self.target_score:
                return True
        return False
    