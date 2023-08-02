from enum import Enum

class Dungeon_type(Enum):
        GIANT = 1
        DRAGON = 2
        NECRO = 3
        FORTRESS = 4
        CRYPT = 5
        R5 = 6

default_donjon = Dungeon_type.GIANT.value