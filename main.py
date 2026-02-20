from CONSTANTS import *
from game import *
from deck import *
from player import *


def main():
    new_game = GameState(player_count=0, target_score=0, round_number=0, player_list={})
    new_game.setup()
    game_deck = Deck()
    while True:     # LOOP 1 - Actual game loop, broken only on victory
        active_players = []
        game_deck.deck_check()  #check to ensure deck isn't empty
        new_game.round_number = new_game.round_number + 1   #new round, so increase round number
        for player in new_game.player_list.values():    # Everyone gets a card to start
            player.hand.append(game_deck.deal_card())
        active_players = list(new_game.player_list.values())
        while len(active_players) > 0:  # LOOP 2 - Round Loop, broken once all players have either "stood" or "bust"
            for player in active_players: #LOOP 3 - iterates through all players to pick their actions.
                print(f"\n{player.player_name}'s current score: {player.score}\n {player.player_name}'s hand:\n") # displays player's current game state
                print(f"[{player.hand}]")
                decision = player.get_action() # asks human what to do/ runs CPU script
                match decision:
                    case "hit":
                        player.hand.append(game_deck.deal_card()) #get a card from the top
                        print(player.hand)
                        player.round_active = player.player_bust_check() # check to see if the player bust
                        match player.round_active:
                            case True: # player didn't bust, remains an active player
                                pass
                            case False: # player bust, delete their current hand, remove them from the rest of the round and commiserate!
                                print("Unlucky! You've bust!")
                                player.hand = []
                    case "stand": # bank your current score, reset the hand and sit out of the rest of the round.
                        player.score += sum(player.hand)
                        player.hand = []
                        player.round_active = False
                game_deck.deck_check()  #check to ensure deck isn't empty
            active_players = [p for p in new_game.player_list.values() if p.round_active]            
        if new_game.victory_check() == True:
            print("GAME OVER!")
            for player in new_game.player_list.values():
                print(f"{player.player_name}'s score: {player.score}\n")
            break     

if __name__ == "__main__":
    main()