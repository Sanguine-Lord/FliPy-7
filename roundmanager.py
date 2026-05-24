from player import *
from cardeffects import *
from game import *
from UiManager import *
import blessedterm as bt

def run_round(game_state: GameState, active_players: list):
        for player in active_players:
            if player.round_active == True: # double check no players have been made inactive since the active_player list was created.
                game_state.ui.player_update(player)
                decision = player.get_action(game_state.ui) 
                match decision:
                    case "hit":
                        game_state.ui.game_update("Hit! Best of luck!", bt.term.white)
                        get_card_effect(game_state, player) # get a card from the top, and do what it says.
                        game_state.ui.player_update(player)
                        round_reset(player.flip_7_check(game_state.game_deck, game_state.ui), active_players) # check to see if the player has 7 cards in hand.
                        player.round_active = player.player_bust_check() # check to see if the player bust
                        match player.round_active:
                            case True: # player didn't bust, remains an active player
                                pass
                            case False: # player bust, delete their current hand, remove them from the rest of the round and commiserate!
                                game_state.ui.game_update("Unlucky! You've bust!", bt.term.white)
                                player.clear_hand(game_state.game_deck)
                    case "stand": # bank your current score, reset the hand and sit out of the rest of the round.
                        game_state.ui.game_update("Stand! Cash those points!", bt.term.white)
                        player.update_score()
                        player.clear_hand(game_state.game_deck)
                        player.round_active = False
        active_players = [p for p in game_state.player_list.values() if p.round_active]
        game_state.ui.player_update(player)
        return active_players     

def round_reset(check: bool, active_players):
    if check == True:
        for player in active_players:
            if player.round_active == True:
                player.round_active = False
                player.update_score()
                player.clear_hand()
    else:
        pass