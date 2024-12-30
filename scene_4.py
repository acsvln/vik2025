from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Print, Stars
from asciimatics.renderers import FigletText, StaticRenderer

from assets import *
from utils import *


def scene_4(screen, duration):
    screen_center_x = screen.width // 2
    screen_center_y = screen.height // 2

    y_bear = screen_center_y - textBlockHeight(bear_rus) // 2 + 5
    y_me2 = textBlockHeight(map_russia) - 10

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
            y=y_bear,
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
            y=y_me2,
            transparent=False,
            clear=True,
            colour=Screen.COLOUR_RED,
            bg=Screen.COLOUR_BLACK
        ),
        Stars( screen,200 )
    ]

    scene = Scene(effects, duration)

    return scene