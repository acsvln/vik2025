# Экран 1: happy new 2025 year, Viktoriia Almazova
# - bird
# - figlet
# - coffe2

# Экран 2: Come back China -> Russia
# - map_china
# - leader_ch
# - plane

# Экран 3: The homeland is waiting for you (me too)
# - map_russia
# - leader_rus

# Экран 4
# - coffe1 по центру
# - happy_new_year_ch
# - dogs1 - 4 бегают внизу
# - parrot1 летит наверху
#  snake


from asciimatics.screen import ManagedScreen

from scene_1 import *
from scene_2 import *
from scene_4 import *
from scene_5 import *
# from scene_nature_fish import *
# from scene_nature_birds import *
# from scene_commie import *
# from scene_ussr import *


@ManagedScreen
def run_the_show(screen=None):
    screen.play([
        scene_1(screen, 40),
        scene_2(screen, 80),
        scene_2_1(screen, 80),
        scene_4(screen, 80),
        scene_5(screen, 80),
    ], stop_on_resize=False)


if __name__ == "__main__":
    run_the_show()