from dataclasses import *

@dataclass
class Player:
    p_type: str
    hand: list = field(default_factory=list)
    score: int
    round_active: bool

    def get_action(self, self.hand):
        raise NotImplementedError("Subclasses must implement get_action")

class Human_Player(Player):
    def get_action(self, self.hand):