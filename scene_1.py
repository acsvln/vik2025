from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Print, Effect
from asciimatics.renderers import FigletText, StaticRenderer

from assets import *
from utils import *


def scene_1(screen, duration):
    screen_center = screen.width // 2

    x_b = screen_center - textBlockWidth(bird) // 2
    y_b = screen_center - textBlockHeight(bird) // 2

    effects = [
        Print(
            screen,
            StaticRenderer([bird]),
            x=x_b + 10,
            y=10,
            colour=Screen.COLOUR_YELLOW
        ),
        Print(
            screen,
            FigletText('Happy new year', font='calgphy2'),
            x=2,
            y=0,
            transparent=True,
            clear=True,
            colour=Screen.COLOUR_WHITE
        ),
        Print(
            screen,
            FigletText('2025', font='poison'),
            x=18,
            y=28,
            transparent=True,
            clear=True,
            colour=Screen.COLOUR_BLUE
        ),
        Print(
            screen,
            FigletText('Viktoriia Almazova', font='big'), #
            x=38,
            y=45,
            transparent=True,
            clear=True,
            colour=Screen.COLOUR_GREEN
        ),
        Print(
            screen,
            StaticRenderer([coffe2]),
            x=123,
            y=42,
            colour=Screen.COLOUR_RED
        )
    ]

    scene = Scene(effects, duration)

    return scene