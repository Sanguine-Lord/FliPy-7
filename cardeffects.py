from game import GameState
from deck import *
from player import *

def get_card_effect(game_state: GameState, player: Player):
    game_state.games_deck.deck_check()
    top_card = game_state.game_deck.deal_card()
    if isinstance(top_card, int):
        player.hand.append(top_card)
    else:
        player.s_hand.append(top_card) 
        match top_card:
            case "F":
                if isinstance(player, Human_Player) is True:
                    target = f"player_{int(input("you've drawn a freeze! Please select a player to lock out of the round! (Enter Player No.)"))}"
                else:
                    active_players = [p for p in game_state.player_list.values() if p.round_active]
                    leader = max(active_players, key=lambda p: p.score) if active_players else None
                    target = leader.player_name
                freeze(game_state, target)
            case "D":
                if isinstance(player, Human_Player) is True:
                    target = f"player_{int(input("you've drawn a Draw-3! Please select a player to force to draw 3 cards! (Enter Player No.)"))}"
                else:
                    if len(player.hand) <= 3:
                        target = player.player_name
                    else:
                        active_players = [p for p in game_state.player_list.values() if p.round_active]
                        leader = max(active_players, key=lambda p: len(p.hand)) if active_players else None
                        target = leader.player_name
                draw_3(game_state, target)
            case "S":
                print("You've drawn a second chance! The next time you bust, this card will be consumed instead!")
                pass
            case "+2":
                print("+2 points!")
                pass
            case "+4":
                print("+4 points!")
                pass
            case "+6":
                print("+6 points!")
                pass
            case "+8":
                print("+8 points!")
                pass
            case "+10":
                print("+10 points!")
                pass
            case "x2":
                print("double points! This only applies to your normal score.")
                pass                                                    
                        
def freeze(game_state: GameState, target: str):
    game_state.player_list[target].score += sum(game_state.player_list[target].hand)
    game_state.player_list[target].clear_hand(game_state.game_deck)
    game_state.player_list[target].round_active = False

def draw_3(game_state: GameState, target: str):
    for _ in range(3):
        get_card_effect(game_state, game_state.player_list[target])
        game_state.player_list[target].round_active = game_state.player_list[target].player_bust_check()
        match game_state.player_list[target].round_active:
            case True: # player didn't bust, remains an active player
                pass
            case False: # player bust, delete their current hand, remove them from the rest of the round and commiserate!
                print("Unlucky! You've bust!")
                game_state.player_list[target].clear_hand(game_state.game_deck)
                game_state.player_list[target].round_active = False
                break     
