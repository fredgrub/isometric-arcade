import arcade
from .city import City
from .constants import *


class Game(arcade.Window):
    """
    Classe principal do jogo, responsável por gerenciar a janela, renderizar o grid
    e lidar com a interação do mouse para seleção de células.
    """

    def __init__(self, width: int, height: int, title: str):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)
        self.mouse_pos = [0, 0]
        self.cartesian_cell = None
        self.isometric_cell = None
        self.cartesian_cell_center = None
        self.city = None

    def setup(self):
        """
        Configure o jogo aqui. Chame essa função para reiniciar o jogo.
        """
        self.city = City()

    def on_draw(self):
        """
        Renderiza o grid e informações de depuração na tela.
        """
        self.clear()
        self.city.grid_sprite_list.draw()

        self.calculate_selected_cell()

        self.city.selected_sprite.center_x, self.city.selected_sprite.center_y = (
            isometric_to_cartesian(*self.isometric_cell)
        )

        self.draw_debug()

    def draw_debug(self):
        start_x = 0
        start_y = SCREEN_SIZE[1] - DEFAULT_LINE_HEIGHT
        arcade.draw_text(
            f"Mouse: {self.mouse_pos[0]}, {self.mouse_pos[1]}",
            start_x,
            start_y,
            arcade.color.WHITE,
            DEFAULT_FONT_SIZE,
            width=SCREEN_SIZE[0],
            align="left",
        )

        start_y -= DEFAULT_LINE_HEIGHT
        arcade.draw_text(
            f"Cell: {self.cartesian_cell[0]}, {self.cartesian_cell[1]}",
            start_x,
            start_y,
            arcade.color.WHITE,
            DEFAULT_FONT_SIZE,
            width=SCREEN_SIZE[0],
            align="left",
        )

        start_y -= DEFAULT_LINE_HEIGHT
        arcade.draw_text(
            f"Selected: {self.isometric_cell[0]}, {self.isometric_cell[1]}",
            start_x,
            start_y,
            arcade.color.WHITE,
            DEFAULT_FONT_SIZE,
            width=SCREEN_SIZE[0],
            align="left",
        )
        # arcade.draw_rectangle_outline(
        #     self.cartesian_cell_center[0],
        #     self.cartesian_cell_center[1],
        #     TILE_SIZE[0],
        #     TILE_SIZE[1],
        #     arcade.color.RED,
        #     2,
        # )

    def on_update(self, delta_time: float):
        pass

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        pass

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.mouse_pos[0] = x
        self.mouse_pos[1] = y

    def calculate_selected_cell(self):
        self.cartesian_cell = [
            self.mouse_pos[0] // TILE_SIZE[0],
            self.mouse_pos[1] // TILE_SIZE[1],
        ]

        self.isometric_cell = [
            (self.cartesian_cell[1] - ISOMETRIC_ORIGIN_IN_CARTESIAN[1])
            + (self.cartesian_cell[0] - ISOMETRIC_ORIGIN_IN_CARTESIAN[0]),
            (self.cartesian_cell[1] - ISOMETRIC_ORIGIN_IN_CARTESIAN[1])
            - (self.cartesian_cell[0] - ISOMETRIC_ORIGIN_IN_CARTESIAN[0]),
        ]

        self.cartesian_cell_center = [
            (self.cartesian_cell[0] + 0.5) * TILE_SIZE[0],
            (self.cartesian_cell[1] + 0.5) * TILE_SIZE[1],
        ]

        p3 = (self.mouse_pos[0], self.mouse_pos[1])

        if self.mouse_pos[0] >= self.cartesian_cell_center[0]:
            if self.mouse_pos[1] >= self.cartesian_cell_center[1]:
                corner1 = (
                    self.cartesian_cell_center[0],
                    self.cartesian_cell_center[1] + TILE_SIZE[1] // 2,
                )
                corner2 = (
                    self.cartesian_cell_center[0] + TILE_SIZE[0] // 2,
                    self.cartesian_cell_center[1],
                )
                sign = get_acute_angle_sign(corner1, corner2, self.mouse_pos)
                if sign >= 0:
                    self.isometric_cell = (
                        self.isometric_cell[0] + 1,
                        self.isometric_cell[1],
                    )
            else:
                corner1 = (
                    self.cartesian_cell_center[0] + TILE_SIZE[0] // 2,
                    self.cartesian_cell_center[1],
                )
                corner2 = (
                    self.cartesian_cell_center[0],
                    self.cartesian_cell_center[1] - TILE_SIZE[1] // 2,
                )
                sign = get_acute_angle_sign(corner1, corner2, p3)
                if sign >= 0:
                    self.isometric_cell = (
                        self.isometric_cell[0],
                        self.isometric_cell[1] - 1,
                    )
        else:
            if self.mouse_pos[1] >= self.cartesian_cell_center[1]:
                corner1 = (
                    self.cartesian_cell_center[0] - TILE_SIZE[0] // 2,
                    self.cartesian_cell_center[1],
                )
                corner2 = (
                    self.cartesian_cell_center[0],
                    self.cartesian_cell_center[1] + TILE_SIZE[1] // 2,
                )
                sign = get_acute_angle_sign(corner1, corner2, p3)
                if sign >= 0:
                    self.isometric_cell = (
                        self.isometric_cell[0],
                        self.isometric_cell[1] + 1,
                    )
            else:
                corner1 = (
                    self.cartesian_cell_center[0],
                    self.cartesian_cell_center[1] - TILE_SIZE[1] // 2,
                )
                corner2 = (
                    self.cartesian_cell_center[0] - TILE_SIZE[0] // 2,
                    self.cartesian_cell_center[1],
                )
                sign = get_acute_angle_sign(corner1, corner2, p3)
                if sign >= 0:
                    self.isometric_cell = (
                        self.isometric_cell[0] - 1,
                        self.isometric_cell[1],
                    )
