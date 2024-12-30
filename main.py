from asciimatics.screen import ManagedScreen

from scene_1 import *
from scene_2 import *
from scene_3 import *
from scene_4 import *
from scene_5 import *

@ManagedScreen
def run_the_show(screen=None):
    screen.play([
        # scene_1(screen, 80),
        scene_2(screen, 40),
        scene_3(screen, 120),
        scene_4(screen, 80),
        # scene_5(screen, -1),
    ], stop_on_resize=False)


if __name__ == "__main__":
    run_the_show()