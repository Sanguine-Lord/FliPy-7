from dataclasses import dataclass, field
from random import *
from player import *
from deck import *

@dataclass
class GameState:
    player_count: int
    round_number: int
    target_score: int
    game_deck: Deck
    player_list: dict = field(default_factory=dict)

    def setup(self):
        player_type = 0
        self.target_score = int(input("What is the score you would like to play to? Default game is 200 points"))
        self.player_count = int(input("How many players are there?"))
        for i in range(1, self.player_count + 1):
            player_type = int(input(f"What type of player is player_{i}? 0 = human, 1 = CPU"))
            match player_type:
                case 0:
                    self.player_list[f"player_{i}"] = Human_Player(score=0, round_active=True, player_name=f"player_{i}")
                case 1:
                    self.player_list[f"player_{i}"] = CPU_Player(score=0, round_active=True, player_name=f"player_{i}")
        self.game_deck.create_deck()

    def run_round(self,active_players):
            for player in active_players: 
                print(f"\n{player.player_name}'s current score: {player.score}\n {player.player_name}'s hand:\n") # displays player's current game state
                print(f"[{player.hand}]")
                decision = player.get_action() 
                match decision:
                    case "hit":
                        print("Hit! Best of luck!")
                        self.apply_card_rules(player) # get a card from the top, and do what it says.
                        print(player.hand)
                        player.round_active = player.player_bust_check() # check to see if the player bust
                        match player.round_active:
                            case True: # player didn't bust, remains an active player
                                pass
                            case False: # player bust, delete their current hand, remove them from the rest of the round and commiserate!
                                print("Unlucky! You've bust!")
                                self.clear_hand(player.hand)
                    case "stand": # bank your current score, reset the hand and sit out of the rest of the round.
                        print("Stand! Cash those points!")
                        player.score += sum(player.hand)
                        self.clear_hand(player.hand, self.game_deck.discard_pile)
                        player.round_active = False
            active_players = [p for p in self.player_list.values() if p.round_active]
            return active_players          

    def victory_check(self):
        for player in self.player_list.values():
            if player.score >= self.target_score:
                return True
        return False
    
    def clear_hand(self, player_hand: list):
            self.game_deck.discard_pile.extend(player_hand)
            player_hand.clear()

    def apply_card_rules(self, player):
        top_card = self.game_deck.deal_card()
        if isinstance(top_card, int):
            player.hand.append(top_card)
        else:
            player.s_hand.append(top_card)
            match top_card:
                case "F":
                    target = f"player_{int(input("you've drawn a freeze! Please select a player to lock out of the round! (Enter Player No.)"))}"
                    self.player_list[target].score += sum(self.player_list[target].hand)
                    self.clear_hand(self.player_list[target].hand)
                    self.player_list[target].round_active = False
                case "D":
                    target = f"player_{int(input("you've drawn a Draw-3! Please select a player to force to draw 3 cards! (Enter Player No.)"))}"
                    for _ in range(3):
                        self.apply_card_rules(self.player_list[target])
                        self.player_list[target].round_active = self.player_list[target].player_bust_check()
                        match self.player_list[target].round_active:
                            case True: # player didn't bust, remains an active player
                                pass
                            case False: # player bust, delete their current hand, remove them from the rest of the round and commiserate!
                                print("Unlucky! You've bust!")
                                self.player_list[target].clear_hand(self.player_list[target].hand)
                                break
                case "S":
                    pass
                case "+2":
                    pass
                case "+4":
                    pass
                case "+6":
                    pass
                case "+8":
                    pass
                case "+10":
                    pass
                case "x2":
                    pass

