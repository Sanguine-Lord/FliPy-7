from dataclasses import *
from deck import Deck

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
                    for x in range(0, len(self.s_hand)):
                        if self.s_hand[x] == "S":
                            print("Second chance consumed! Be more careful from now on!")
                            self.s_hand[x] = ""
                            self.hand.remove(self.hand[i])
                            return True
                    return False
        return True
    
    def update_score(self):
        special_score = 0
        for i in range(0, len(self.s_hand)):
            match i:
                case "+2":
                    special_score += 2
                case "+4":
                    special_score += 4
                case "+6":
                    special_score += 6
                case "+8":
                    special_score += 8
                case "+10":
                    special_score += 10
                case "x2":
                    special_score += sum(self.hand)                
        self.score += sum(self.hand) + special_score
        
    def clear_hand(self, deck: Deck):
        deck.discard_pile.extend(self.hand)
        deck.discard_pile.extend(self.s_hand)
        self.hand.clear()
        self.s_hand.clear()
    

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

