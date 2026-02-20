from dataclasses import *
from random import *

@dataclass
class Deck():
    current_deck: list = field(default_factory=list)

    def create_deck(self):
        self.current_deck = []
        for i in range(12,1,-1):
            for j in range (0,i):
                self.current_deck.append(i)
        self.current_deck.append(0)
        shuffle(self.current_deck)
        return self.current_deck

    def deal_card(self):
        top_card = self.current_deck.pop()
        return top_card
    
    def deck_check(self):
        if self.current_deck == []:
            self.create_deck()
        else:
            pass
