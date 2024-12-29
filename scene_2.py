from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Print
from asciimatics.renderers import FigletText, StaticRenderer

from assets import *

def scene_2(screen, duration):
    effects = [
        Print(
            screen,
            StaticRenderer([map_china]),
            x=39,
            y=10,
            colour=Screen.COLOUR_RED
        ),
        Print(
            screen,
            StaticRenderer([leader_ch]),
            x=20,
            y=8,
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


