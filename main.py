from CONSTANTS import *
from game import *
from random import *


def main():
    new_game = GameState(playercount=4, deck=[])
    new_game.createdeck()

if __name__ == "__main__":
    main()