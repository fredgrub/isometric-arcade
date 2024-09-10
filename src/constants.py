# Window dimensions
SCREEN_SIZE = (1280, 640)
SCREEN_TITLE = "My Game"

# Isometric grid
WORLD_SIZE = (10, 10)
TILE_SIZE = (64, 32)
ISOMETRIC_ORIGIN_IN_CARTESIAN = (10, 2)

# Text
DEFAULT_FONT_SIZE = 18
DEFAULT_LINE_HEIGHT = 30


def isometric_to_cartesian(x, y):
    screen_x = (
        (ISOMETRIC_ORIGIN_IN_CARTESIAN[0] * TILE_SIZE[0]) + (x - y) * TILE_SIZE[0] // 2
    ) + TILE_SIZE[0] // 2
    screen_y = (
        (ISOMETRIC_ORIGIN_IN_CARTESIAN[1] * TILE_SIZE[1]) + (x + y) * TILE_SIZE[1] // 2
    ) + TILE_SIZE[1] // 2
    return (screen_x, screen_y)


def get_acute_angle_sign(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
