from dataclasses import *
import blessedterm as bt

@dataclass
class UI:
    player_zones: dict = field(default_factory = lambda: 
                               {"player_1": {"y": 2, "colour": bt.term.cyan},
                                "player_2": {"y": 7, "colour": bt.term.magenta},
                                "player_3": {"y": 12, "colour": bt.term.green},
                                "player_4": {"y": 17, "colour": bt.term.yellow},
                                "player_5": {"y": 22, "colour": bt.term.white}})

    def text_prompt(self, prompt) -> str:
        bt.clear_area(0, 25)
        response = bt.get_input(0, 25, f"{prompt}: ")
        return str(response)


    def int_prompt(self, prompt) -> int:
        bt.clear_area(0, 25)
        response = bt.get_input(0, 25, f"{prompt}: ")
        
        try:
            return int(response)
        except ValueError:
            bt.draw_text(0, 24, "That wasn't a number!", bt.term.red)
            return self.int_prompt(prompt)

    def player_update(self, player):
        zone = self.player_zones[player.player_name]
        y = zone["y"]
        colour = zone["colour"]

        bt.clear_area(0 , y)
        bt.draw_text(0 , y, f"{player.player_name} | Score: {player.score}", colour)

        bt.clear_area(0 , y + 1)
        bt.draw_text(0 , y + 1, f"Current Hand: {player.hand}", colour)

        bt.clear_area(0 , y + 2)
        bt.draw_text(0 , y + 2, f"Current Special Cards: {player.s_hand}", colour)        

        bt.clear_area(0 , y + 3)
        bt.draw_text(0 , y + 3, f"Status: {player.round_active}")

    def game_update(self, text, colour):
        bt.clear_area(0, 25)
        bt.draw_text(0, 25, text, colour)

