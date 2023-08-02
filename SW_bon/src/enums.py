from enum import Enum

class Dungeon_type(Enum):
        NONE = 0
        GIANT = 1
        DRAGON = 2
        SPIRITUAL_REALM = 3
        NECRO = 4
        FORTRESS = 5
        CRYPT = 6
        R5 = 7
        FIRE_RIFT = 8
        WATER_RIFT = 9
        WIND_RIFT = 10
        LIGHT_RIFT = 11
        DARK_RIFT = 12

class Dimension_type(Enum):
        NONE = 12
        KARZHAN = 13

default_donjon = Dungeon_type.GIANT.value