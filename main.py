import arcade
import src.game as game
from src.constants import *

def main():
    window = game.Game(SCREEN_SIZE[0], SCREEN_SIZE[1], SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()