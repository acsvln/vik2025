# Экран 1: happy new 2025 year, Viktoriia Almazova
# - bird
# - figlet
# - coffe2 -> snake

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


from asciimatics.screen import ManagedScreen

from scene_1 import *
# from scene_nature_fish import *
# from scene_nature_birds import *
# from scene_commie import *
# from scene_ussr import *


@ManagedScreen
def run_the_show(screen=None):
    screen.play([
        scene_1(screen, 40),
        # scene_nature_fish(screen, 80),
        # scene_nature_birds(screen, 80),
        # scene_commie(screen, 50),
        # scene_ussr(screen, -1)
    ], stop_on_resize=False)


if __name__ == "__main__":
    run_the_show()