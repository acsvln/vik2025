from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Print, Effect
from asciimatics.effects import Print, Sprite

from asciimatics.paths import Path
from asciimatics.renderers import FigletText, StaticRenderer

from assets import *
from utils import *


def scene_2(screen, duration):
    screen_center = screen.width // 2

    x_b = screen_center - textBlockWidth(bird) // 2
    y_b = screen_center - textBlockHeight(bird) // 2

    effects = [
        Print(
            screen,
            StaticRenderer([map_china]),
            x=x_b + 10,
            y=10,
            colour=Screen.COLOUR_RED
        ),
        Print(
            screen,
            StaticRenderer([leader_ch]),
            x=20,
            y=6,
            colour=Screen.COLOUR_RED
        ),
        Print(
            screen,
            FigletText('Come back China -> Russia', font='big'),
            x=12,
            y=0,
            transparent=True,
            clear=True,
            colour=Screen.COLOUR_WHITE
        ),
    ]

    scene = Scene(effects, duration)

    return scene


