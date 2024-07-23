from dataclasses import dataclass
from typing import TextIO

from .exceptions import NotAnObjectError
from .obj import Object


@dataclass
class Level:
    name: str
    date: float
    objects: list[Object]
    settings: dict[str, str]
    layers: dict[str, str]

    @classmethod
    def loads(cls, string: str, level_name: str):
        objects = []
        layers = {}

        lines = [
            line
            for line in string.split('\n')
            if not (line.startswith('//') and line.endswith('//')) and line
        ]

        # first line in the date
        date = float(lines[0].split(',')[1])

        # block of layer names
        idx = 0
        for idx, line in enumerate(lines[1:]):
            if not line.lstrip().startswith('layerName,'):
                break
            _, layer_id, layer_name, *_ = line.split(',')
            layers[layer_id] = layer_name

        # the line after the layers are the settings
        # TODO: level settings are not done yet
        settings = {'TODO': lines[idx + 1]}

        # everything else are objects
        for line in lines[idx + 2 :]:
            # HACK: HLD level files include broken objects
            # and hldlib should be able to load all vanilla HLD files
            try:
                objects.append(Object.from_string(line))
            except NotAnObjectError as err:
                from sys import stderr

                stderr.write(f'broken object loaded: {err!r}')
                stderr.write('\n')

        return cls(level_name, date, objects, settings, layers)

    @classmethod
    def load(cls, f: TextIO, level_name: str):
        return cls.loads(f.read(), level_name)
