from enum import Enum


class HLDDirection(str, Enum):
    """
    Enum with all HLD regions.
    """

    def __str__(self):
        return self.value
    NORTH = "north"
    EAST = "east"
    WEST = "west"
    SOUTH = "south"
    CENTRAL = "central"
    INTRO = "intro"
    ABYSS = "abyss"
    CHALLENGES = "challenges"
    EXTRA = "extra"
    TESTLEVELS = "testlevels"
    NONE = "none"
