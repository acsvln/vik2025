from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.particles import PalmFirework, RingExplosion, RingFirework, SerpentFirework
from asciimatics.effects import Print, Sprite

from asciimatics.paths import Path
from asciimatics.renderers import FigletText, StaticRenderer

from assets import *
from utils import *


def scene_5(screen, duration):
    screen_center_x = screen.width // 2
    screen_center_y = screen.height // 2

    int_width = screen_center_x - textBlockWidth( happy_new_year_ch ) // 2 - 11
    int_width2 = screen_center_x -  textBlockWidth( snake ) // 2 + 10
    int_height = screen_center_y - ( textBlockHeight( happy_new_year_ch ) + textBlockHeight( snake ) ) // 2

    path_dog1 = Path()
    path_dog1.jump_to(screen.width, 42)
    path_dog1.move_straight_to(0, 42, 80)

    path_dog4 = Path()
    path_dog4.jump_to(0, 44)
    path_dog4.move_straight_to(screen.width, 44, 20)

    path_dog5 = Path()
    path_dog5.jump_to(screen.width, 46)
    path_dog5.move_straight_to( 0, 46, 35)

    path_dog2 = Path()
    path_dog2.jump_to(screen.width, 49)
    path_dog2.move_straight_to(0, 49, 80)

    path_dog3 = Path()
    path_dog3.jump_to(0, 51)
    path_dog3.move_straight_to(screen.width, 51, 30)

    path_parrot = Path()
    path_parrot.jump_to(0, 10)
    path_parrot.move_straight_to(screen.width, 10, 100)

    effects = [
        Print(
            screen,
            StaticRenderer( [ snake ] ),
            x=int_width,
            y=int_height,
            colour=Screen.COLOUR_GREEN
        ),
        Print(
            screen,
            StaticRenderer( [ happy_new_year_ch ] ),
            x=int_width2 + 3,
            y=int_height + 19,
            colour=Screen.COLOUR_GREEN
        ),
        Sprite(
            screen,
            renderer_dict={ "default": StaticRenderer([dogs1]) },
            path=path_dog1,
            clear=True,
            colour=Screen.COLOUR_MAGENTA
        ),
        Sprite(
            screen,
            renderer_dict = { "default": StaticRenderer([dogs2]) },
            path=path_dog2,
            clear=True,
            colour=Screen.COLOUR_CYAN
        ),
        Sprite(
            screen,
            renderer_dict={ "default": StaticRenderer([dogs3]) },
            path=path_dog3,
            clear=True,
            colour=Screen.COLOUR_MAGENTA
        ),
        Sprite(
            screen,
            renderer_dict={ "default": StaticRenderer([dogs4]) },
            path=path_dog4,
            clear=True,
            colour=Screen.COLOUR_CYAN
        ),
        Sprite(
            screen,
            renderer_dict={"default": StaticRenderer([dogs5])},
            path=path_dog5,
            clear=True,
            colour=Screen.COLOUR_CYAN
        ),
        Sprite(
            screen,
            renderer_dict={"default": StaticRenderer([parrot1])},
            path=path_parrot,
            clear=True,
            colour=Screen.COLOUR_CYAN
        ),
        SerpentFirework(
            screen, x=20, y=25, life_time=1000
        ),
        SerpentFirework(
            screen, x=screen.width - 20, y=15, life_time=1000
        ),
    ]



    scene = Scene(effects, duration)

    return scene