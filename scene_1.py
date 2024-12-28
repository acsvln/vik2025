from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Print
from asciimatics.renderers import FigletText, StaticRenderer

from assets import *
from utils import *


def scene_1(screen, duration):
    screen_center_x = screen.width // 2
    screen_center_y = screen.height // 2

    x_b = screen_center_x - textBlockWidth(bird) // 2 + 10
    y_b = 10

    x_hp_year = x_b - 8
    y_hp_year = y_b + textBlockHeight(bird) // 2 - 1

    x_vik = x_b
    y_vik = y_b + textBlockHeight(bird)  - 8

    x_coff = x_vik + 86
    y_coff = y_vik - 3

    effects = [
        Print(
            screen,
            StaticRenderer([bird]),
            x = x_b,
            y = y_b,
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
            x=x_hp_year,
            y=y_hp_year,
            transparent=True,
            clear=True,
            colour=Screen.COLOUR_BLUE
        ),
        Print(
            screen,
            FigletText('Viktoriia Almazova', font='big'), #
            x=x_vik,
            y=y_vik,
            transparent=True,
            clear=True,
            colour=Screen.COLOUR_GREEN
        ),
        Print(
            screen,
            StaticRenderer([coffe2]),
            x=x_coff,
            y=y_coff,
            colour=Screen.COLOUR_RED
        )
    ]

    scene = Scene(effects, duration)

    return scene