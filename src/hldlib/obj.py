import re
from dataclasses import dataclass

from .exceptions import NotAnObjectError
from .objecttypes import ObjectType

OBJ_REGEX = re.compile(
    r'obj,(?P<type>.+?),(?P<id>\d+),(?P<x>[\d-]+),'
    r'(?P<y>[\d-]+),(?P<layer>[\d-]+),'
    r'(?:\d+,(?P<depends>(?:\d+,)*\d+)|-999999)'
    r'(?:,caseScript,(?P<cid>[0-4]),(?P<invert>.+?),'
    r'(?P<actor>.+?),(?P<delay>\d+)|)'
    r',\+\+,(?P<attrs>.*)'
)


def split_attrs(string: str) -> dict[str, str]:
    if not string:
        return {}
    keqvs = string.split(',')
    return {k: v for k, v in [keqv.split('=') for keqv in keqvs if keqv]}


def join_attrs(attrs: dict[str, str]) -> str:
    return ','.join([f'{k}={v}' for k, v in attrs.items()])


@dataclass
class Casescript:
    id: int
    invert: bool
    actor: ObjectType
    delay: int


@dataclass
class Object:
    type: ObjectType
    id: int
    x: int
    y: int
    layer: int
    depends: list[int]
    cs: Casescript | None
    attrs: dict[str, str]

    @classmethod
    def from_string(cls, string: str):
        match = OBJ_REGEX.search(string)
        if match is None:
            raise NotAnObjectError(
                f'passed in string is not an object: {string.strip()}'
            )

        obj_dict = match.groupdict()
        type_ = ObjectType(obj_dict['type'])
        id = int(obj_dict['id'])
        x = int(obj_dict['x'])
        y = int(obj_dict['y'])
        layer = int(obj_dict['layer'])
        attrs = split_attrs(obj_dict['attrs'])

        depends = []
        if obj_dict['depends']:
            depends = [int(v) for v in obj_dict['depends'].split(',')]

        cs = None
        if obj_dict['delay']:
            cid = int(obj_dict['cid'])
            # there is only one case of this happening
            # but we cannot leave it unhandled
            if obj_dict['invert'] == 'false':
                invert = False
            else:
                invert = bool(int(obj_dict['invert']))
            # also special cases that should be handled
            if obj_dict['actor'] in {'-1', '0', '1'}:
                actor = ObjectType.NONE
            else:
                actor = ObjectType(obj_dict['actor'])
            delay = int(obj_dict['delay'])
            cs = Casescript(cid, invert, actor, delay)

        return cls(type_, id, x, y, layer, depends, cs, attrs)
