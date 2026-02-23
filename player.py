from dataclasses import *

@dataclass
class Player:
    score: int
    round_active: bool
    player_name: str
    hand: list = field(default_factory=list)
    s_hand: list = field(default_factory=list)


    def get_action(self):
        raise NotImplementedError("Subclasses must implement get_action")
    
    def player_bust_check(self):
        for i in range(0, len(self.hand)):
            for j in range(i + 1, len(self.hand)):
                if self.hand[i] == self.hand[j]:
                    return False
        return True
    

class Human_Player(Player):
    def get_action(self):
        decision = input("What would you like to do? 'h' for Hit and 's' for Stand\n")
        match decision:
            case "h":
                return "hit"
            case "s":
                return "stand"
            case _:
                print("Input not valid! Automatically standing")
                return "stand"
        
class CPU_Player(Player):
    def get_action(self):
        if len(self.hand) < 3:
            return "hit"
        elif sum(self.hand) > 30:
            return "stand"
        else:
            return "hit"

