from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Print, Effect
from asciimatics.effects import Print, Sprite

from asciimatics.paths import Path
from asciimatics.renderers import FigletText, StaticRenderer

from assets import *
from utils import *


def scene_4(screen, duration):
    screen_center = screen.width // 2

    x_b = screen_center - textBlockWidth(bird) // 2
    y_b = screen_center - textBlockHeight(bird) // 2

    effects = [
        Print(
            screen,
            StaticRenderer([map_russia]),
            x=0,
            y=0,
            colour=Screen.COLOUR_BLUE
        ),
        Print(
            screen,
            StaticRenderer([leader_rus]),
            x=100,
            y=19,
            colour=Screen.COLOUR_GREEN,
            clear=True,
            transparent=False
        ),
        Print(
            screen,
            FigletText('The homeland is waiting for you', font='standard', width=160 ),
            x=0,
            y=0,
            transparent=False,
            clear=True,
            colour=Screen.COLOUR_WHITE,
            bg=Screen.COLOUR_BLACK
        ),
        # Print(
        #     screen,
        #     FigletText('(mee too)', font='stop', width=160),
        #     x=58,
        #     y=6,
        #     transparent=False,
        #     clear=True,
        #     colour=Screen.COLOUR_RED,
        #     bg=Screen.COLOUR_BLACK
        # ),
        Print(
            screen,
            FigletText('(mee too)', font='stop', width=160),
            x=58,
            y=6,
            transparent=False,
            clear=True,
            colour=Screen.COLOUR_RED,
            bg=Screen.COLOUR_BLACK
        ),
    ]



    scene = Scene(effects, duration)

    return scene