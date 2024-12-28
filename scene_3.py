from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Print, Effect
from asciimatics.effects import Print, Sprite

from asciimatics.paths import Path
from asciimatics.renderers import FigletText, StaticRenderer

from assets import *
from utils import *

def scene_3(screen, duration):
    screen_center = screen.width // 2

    x_b = screen_center - textBlockWidth(bird) // 2
    y_b = screen_center - textBlockHeight(bird) // 2

    path = Path()
    path.jump_to(x_b + 10, screen.height // 2)
    path.move_straight_to(screen.width, screen.height // 2, 60)

    path1 = Path()
    path1.jump_to(x_b + 50, 30)
    path1.move_straight_to(-50, 30, 60)

    path2 = Path()
    path2.jump_to(x_b + 350, 30)
    path2.move_straight_to(-35, 30, 60)

    effects = [
        Sprite(
            screen,
            renderer_dict={
                "default": StaticRenderer(
                    [map_china] * 24
                )
            },
            path=path1,
            clear=False,
            colour=Screen.COLOUR_RED
        ),
        Sprite(
            screen,
            renderer_dict={
                "default": StaticRenderer(
                    [map_russia] * 140
                )
            },
            path=path2,
            clear=False,
            colour=Screen.COLOUR_BLUE
        ),
        Sprite(
            screen,
            renderer_dict={
                "default": StaticRenderer(
                    [plane] * 12
                )
            },
            path=path,
            clear=False  # ,
            # colour=Colour
        )
    ]

    scene = Scene(effects, duration)

    return scene