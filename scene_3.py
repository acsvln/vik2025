from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Sprite

from asciimatics.paths import Path
from asciimatics.renderers import StaticRenderer

from assets import *

def scene_3(screen, duration):
    screen_center_x = screen.width // 2

    path_plane = Path()
    path_plane.jump_to(screen_center_x - 40, screen.height // 2)
    path_plane.move_straight_to(screen.width, screen.height // 2, 60)

    path_china = Path()
    path_china.jump_to(screen_center_x, 30)
    path_china.move_straight_to(-50, 30, 60)

    path_russia = Path()
    path_russia.jump_to(screen_center_x + 300, 26)
    path_russia.move_straight_to(0, 26, 80)

    effects = [
        Sprite(
            screen,
            renderer_dict = { "default": StaticRenderer( [ map_china ] * 14 ) },
            path=path_china,
            clear=False,
            colour=Screen.COLOUR_RED
        ),
        Sprite(
            screen,
            renderer_dict = { "default": StaticRenderer( [ map_russia ] * 14 ) },
            path=path_russia,
            clear=False,
            colour=Screen.COLOUR_BLUE,
        ),
        Sprite(
            screen,
            renderer_dict = { "default" : StaticRenderer( [ plane ] * 12 ) },
            path=path_plane,
            clear=False
        )
    ]

    scene = Scene(effects, duration)

    return scene