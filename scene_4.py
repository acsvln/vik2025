from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Print, Stars
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
            StaticRenderer([bear_rus]),
            x=100,
            y=19,
            colour=Screen.COLOUR_GREEN,
            clear=True,
            transparent=True
        ),
        Print(
            screen,
            FigletText('The homeland is waiting for you', font='standard', width=160 ),
            x=4,
            y=2,
            transparent=False,
            clear=True,
            colour=Screen.COLOUR_WHITE,
            bg=Screen.COLOUR_BLACK
        ),
        Print(
            screen,
            FigletText('mee too...', font='stop', width=160),
            x=10,
            y=43, # screen height
            transparent=False,
            clear=True,
            colour=Screen.COLOUR_RED,
            bg=Screen.COLOUR_BLACK
        ),
        Stars( screen,200 )
    ]

    scene = Scene(effects, duration)

    return scene