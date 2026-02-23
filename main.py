from CONSTANTS import *
from game import *
from deck import *
from player import *


def main():
    new_game = GameState(player_count=0, target_score=0, round_number=0, player_list={}, game_deck=Deck())
    new_game.setup()
    while True:     # LOOP 1 - Actual game loop, broken only on victory
        active_players = []
        new_game.game_deck.deck_check()  # check to ensure deck isn't empty
        new_game.round_number = new_game.round_number + 1   #new round, so increase round number
        for player in new_game.player_list.values():    # Everyone gets a card to start
            new_game.apply_card_rules(player) # get a card from the top, and do what it says.
        active_players = list(new_game.player_list.values())
        while len(active_players) > 0:  # LOOP 2 - Round Loop, broken once all players have either "stood" or "bust"
            active_players = new_game.run_round(active_players)
            new_game.game_deck.deck_check() 
        if new_game.victory_check() == True:
            print("GAME OVER!")
            for player in new_game.player_list.values():
                print(f"{player.player_name}'s score: {player.score}\n")
            break     

if __name__ == "__main__":
    main()