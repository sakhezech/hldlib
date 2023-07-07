import os
import sys
from pathlib import Path

from hldlib.hlddirections import HLDDirection
from hldlib.hlderror import HLDError
from hldlib.hldlevel import HLDLevel


def get_levels_root_folder(path: Path) -> Path:
    match sys.platform:
        case 'win32':
            return path
        case 'linux':
            return path / 'assets'
        case 'darwin':
            return path / 'HyperLightDrifter.app' / 'Contents' / 'Resources'
        case _:
            raise HLDError(f'{sys.platform} is not a supported platform.')


def default_load(path: str | Path) -> list[HLDLevel]:
    """
    Default load method for loading levels from the basic HLD .lvl file structure.

    Gets all levels from path/North, path/East, path/..., path/Abyss
    """
    path = Path(path)
    path_to_levels = get_levels_root_folder(path)
    if sys.platform == 'win32':
        folder_paths = [
            path_to_levels / dir_.capitalize()
            for dir_ in [
                HLDDirection.NORTH,
                HLDDirection.EAST,
                HLDDirection.WEST,
                HLDDirection.SOUTH,
                HLDDirection.CENTRAL,
                HLDDirection.INTRO,
                HLDDirection.ABYSS,
            ]
        ]
    else:
        folder_paths = [
            path_to_levels / dir_
            for dir_ in [
                HLDDirection.NORTH,
                HLDDirection.EAST,
                HLDDirection.WEST,
                HLDDirection.SOUTH,
                HLDDirection.CENTRAL,
                HLDDirection.INTRO,
                HLDDirection.ABYSS,
            ]
        ]
    levels = [
        HLDLevel.load(
            level.path, HLDDirection(Path(level.path).parent.name.lower())
        )
        for paths in [os.scandir(folder) for folder in folder_paths]
        for level in paths
        if level.path.endswith('.lvl')
    ]
    return levels


def default_dump(levels: list[HLDLevel], path: str | Path) -> None:
    path = Path(path)
    for level in levels:
        dump_to = (
            path / level.direction.capitalize()
            if sys.platform == 'win32'
            else path / level.direction
        )
        level.dump(dump_to)


class Counter:
    """
    A simple counter class. Useful for creating new HLDObj's and giving them unique IDs.
    """

    def __init__(self, val: int = 10000):
        self._val = val

    def use(self) -> int:
        self._val += 1
        return self._val
