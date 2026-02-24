from player import *
from cardeffects import *

def run_round(game_state, active_players):
        for player in active_players:
            if player.round_active == True: # double check no players have been made inactive since the active_player list was created.
                print(f"\n{player.player_name}'s current score: {player.score}\n {player.player_name}'s hand:\n") # displays player's current game state
                print(f"[{player.hand}]")
                decision = player.get_action() 
                match decision:
                    case "hit":
                        print("Hit! Best of luck!")
                        get_card_effect(game_state, player) # get a card from the top, and do what it says.
                        print(player.hand)
                        player.round_active = player.player_bust_check() # check to see if the player bust
                        match player.round_active:
                            case True: # player didn't bust, remains an active player
                                pass
                            case False: # player bust, delete their current hand, remove them from the rest of the round and commiserate!
                                print("Unlucky! You've bust!")
                                player.clear_hand(game_state.game_deck)
                    case "stand": # bank your current score, reset the hand and sit out of the rest of the round.
                        print("Stand! Cash those points!")
                        player.update_score()
                        player.clear_hand(game_state.game_deck)
                        player.round_active = False
        active_players = [p for p in game_state.player_list.values() if p.round_active]
        return active_players          