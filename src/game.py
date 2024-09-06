import arcade
from .city import City
from .constants import *

class Game(arcade.Window):
    
    def __init__(self, width: int, height: int, title: str):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)
        self.mouse_x = 0
        self.mouse_y = 0
    
    def setup(self):
        self.city = City()

    def on_draw(self):
        self.clear()
        self.city.grid_sprite_list.draw()

        cell_row = self.mouse_x // TILE_SIZE[0]
        cell_column = self.mouse_y // TILE_SIZE[1]

        selected = (
            (cell_column - ORIGIN[1]) + (cell_row - ORIGIN[0]),
            (cell_column - ORIGIN[1]) - (cell_row - ORIGIN[0])
        )

        xc = (cell_row + 0.5)*TILE_SIZE[0]
        yc = (cell_column + 0.5)*TILE_SIZE[1]

        p3 = (self.mouse_x, self.mouse_y)

        if self.mouse_x >= xc:
            if self.mouse_y >= yc:
                p1 = (xc, yc + TILE_SIZE[1] // 2)
                p2 = (xc + TILE_SIZE[0] // 2, yc)
                cross_product = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
                if cross_product >= 0:
                    selected = (selected[0] + 1, selected[1])
            else:
                p1 = (xc + TILE_SIZE[0] // 2, yc)
                p2 = (xc, yc - TILE_SIZE[1] // 2)
                cross_product = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
                if cross_product >= 0:
                    selected = (selected[0], selected[1] - 1)
        else:
            if self.mouse_y >= yc:
                p1 = (xc - TILE_SIZE[0] // 2, yc)
                p2 = (xc, yc + TILE_SIZE[1] // 2)
                cross_product = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
                if cross_product >= 0:
                    selected = (selected[0], selected[1] + 1)
            else:
                p1 = (xc, yc - TILE_SIZE[1] // 2)
                p2 = (xc - TILE_SIZE[0] // 2, yc)
                cross_product = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
                if cross_product >= 0:
                    selected = (selected[0] - 1, selected[1])

        #arcade.draw_rectangle_outline(xc, yc, TILE_SIZE[0], TILE_SIZE[1], arcade.color.RED, 2)
        self.city.selected_sprite.center_x, self.city.selected_sprite.center_y = self.city.to_screen(*selected)

        start_x = 0
        start_y = SCREEN_SIZE[1] - DEFAULT_LINE_HEIGHT
        arcade.draw_text(f"Mouse: {self.mouse_x}, {self.mouse_y}",
                         start_x,
                         start_y,
                         arcade.color.WHITE,
                         DEFAULT_FONT_SIZE,
                         width=SCREEN_SIZE[0],
                         align="left")
        
        start_y -= DEFAULT_LINE_HEIGHT
        arcade.draw_text(f"Cell: {cell_row}, {cell_column}",
                         start_x,
                         start_y,
                         arcade.color.WHITE,
                         DEFAULT_FONT_SIZE,
                         width=SCREEN_SIZE[0],
                         align="left")
        
        start_y -= DEFAULT_LINE_HEIGHT
        arcade.draw_text(f"Selected: {selected[0]}, {selected[1]}",
                         start_x,
                         start_y,
                         arcade.color.WHITE,
                         DEFAULT_FONT_SIZE,
                         width=SCREEN_SIZE[0],
                         align="left")
        
    def on_update(self, delta_time: float):
        pass

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        pass
    
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.mouse_x = x
        self.mouse_y = y