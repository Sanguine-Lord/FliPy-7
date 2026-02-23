from dataclasses import *
from random import *
from player import *

@dataclass
class Deck():
    current_deck: list = field(default_factory=list)
    discard_pile: list = field(default_factory=list)

    def create_deck(self):
        self.current_deck = []
        for i in range(12,1,-1):
            for j in range (0,i):
                self.current_deck.append(i)
        self.current_deck.append(0)
        for i in range(0, 3):
            self.current_deck.append("F")
            self.current_deck.append("D")
            self.current_deck.append("S")
        for i in range(0, 6):
            self.current_deck.append("+2")
            self.current_deck.append("+4")
            self.current_deck.append("+6")
            self.current_deck.append("+8")
            self.current_deck.append("+10")
            self.current_deck.append("x2")
        shuffle(self.current_deck)

    def deal_card(self):
        top_card = self.current_deck.pop()
        return top_card

    def reset_deck(self):
        self.current_deck = []
        self.current_deck = self.discard_pile
    
    def deck_check(self):
        if self.current_deck == []:
            self.reset_deck()
        else:
            pass
