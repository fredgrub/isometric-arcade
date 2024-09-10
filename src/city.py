import arcade
from .constants import *


class City:

    def __init__(self):
        self.grid = []
        for row in range(WORLD_SIZE[0]):
            self.grid.append([])
            for column in range(WORLD_SIZE[1]):
                self.grid[row].append(0)

        self.grid_sprite_list = arcade.SpriteList()

        for x in reversed(range(WORLD_SIZE[0])):
            for y in reversed(range(WORLD_SIZE[1])):
                sprite_center = isometric_to_cartesian(x, y)
                sprite = arcade.Sprite("assets/grass.png")
                sprite.center_x = sprite_center[0]
                sprite.center_y = sprite_center[1]
                self.grid_sprite_list.append(sprite)

        self.selected_sprite = arcade.Sprite("assets/residence.png")
        self.selected_sprite.center_x = TILE_SIZE[0] // 2
        self.selected_sprite.center_y = TILE_SIZE[1] // 2
        self.grid_sprite_list.append(self.selected_sprite)
