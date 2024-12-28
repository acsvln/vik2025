from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Print, Effect
from asciimatics.effects import Print, Sprite

from asciimatics.paths import Path
from asciimatics.renderers import FigletText, StaticRenderer

from assets import *
from utils import *


def scene_5(screen, duration):
    screen_center = screen.width // 2

    x_b = screen.width // 2 -  textBlockWidth(happy_new_year_ch) // 2
    y_b = screen.height // 2 - textBlockHeight(happy_new_year_ch) // 2


    fish_path_r1 = Path()
    fish_path_r1.jump_to(screen.width, 20)
    fish_path_r1.move_straight_to(0, 20, 40)

    fish_path_r2 = Path()
    fish_path_r2.jump_to(screen.width, 45)
    fish_path_r2.move_straight_to(0, 45, 80)

    fish_path_r3 = Path()
    fish_path_r3.jump_to(screen.width, 54)
    fish_path_r3.move_straight_to(0, 54, 30)

    path_fish_l1 = Path()
    path_fish_l1.jump_to(0, 30)
    path_fish_l1.move_straight_to(screen.width, 30, 20)

    path_fish_l2 = Path()
    path_fish_l2.jump_to(0, 35)
    path_fish_l2.move_straight_to(screen.width, 35, 35)

    effects = [
        Print(
            screen,
            StaticRenderer([happy_new_year_ch, snake]),
            x=x_b,
            y=y_b,
            colour=Screen.COLOUR_GREEN
        ),
        Sprite(
            screen,
            renderer_dict={
                "default": StaticRenderer([dogs1])
            },
            path=fish_path_r1,
            clear=True,
            colour=Screen.COLOUR_MAGENTA
        ),
        Sprite(
            screen,
            renderer_dict={
                "default": StaticRenderer([dogs2])
            },
            path=fish_path_r2,
            clear=True,
            colour=Screen.COLOUR_CYAN
        ),
        Sprite(
            screen,
            renderer_dict={
                "default": StaticRenderer([dogs3])
            },
            path=fish_path_r3,
            clear=True,
            colour=Screen.COLOUR_MAGENTA
        ),
        Sprite(
            screen,
            renderer_dict={
                "default": StaticRenderer([dogs4])
            },
            path=path_fish_l1,
            clear=True,
            colour=Screen.COLOUR_CYAN
        ),
        # Print(
        #     screen,
        #     StaticRenderer([leader_rus]),
        #     x=100,
        #     y=19,
        #     colour=Screen.COLOUR_GREEN,
        #     clear=True,
        #     transparent=False
        # ),
        # Print(
        #     screen,
        #     FigletText('The homeland is waiting for you', font='standard', width=160 ),
        #     x=0,
        #     y=0,
        #     transparent=False,
        #     clear=True,
        #     colour=Screen.COLOUR_WHITE,
        #     bg=Screen.COLOUR_BLACK
        # ),
        # # Print(
        # #     screen,
        # #     FigletText('(mee too)', font='stop', width=160),
        # #     x=58,
        # #     y=6,
        # #     transparent=False,
        # #     clear=True,
        # #     colour=Screen.COLOUR_RED,
        # #     bg=Screen.COLOUR_BLACK
        # # ),
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
    ]



    scene = Scene(effects, duration)

    return scene