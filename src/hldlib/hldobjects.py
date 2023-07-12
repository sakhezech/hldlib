import re
from enum import Enum
from typing import Literal

from hldlib.hlderror import HLDError
from hldlib.hldtype import HLDType


class CaseScriptType(Enum):
    BOOMBOX = 0
    ALL = 1
    REGION = 2
    FLAG = 3
    ENEMY = 4
    NO = 5


class Dependencies:
    def __init__(
        self,
        depends_on: list[int],
        casescript: CaseScriptType,
        inverted: bool,
        actor: HLDType | Literal['-1', '0', '1', '-999999'],
        delay: int,
    ):
        self.depends_on = depends_on
        self.casescript = casescript
        self.inverted = inverted
        self.actor = actor
        self.delay = delay

    @classmethod
    def from_string(cls, string: str):
        before, after, *_ = string.split(',caseScript,') + ['']
        depends_on = [int(num) for num in before.split(',')[1:]]
        if not after:
            caseScriptType = CaseScriptType.NO
            inverted = False
            actor = '-999999'
            delay = 0
        else:
            caseScriptType, inverted, actor, delay = after.split(',')  # type: ignore
            caseScriptType = CaseScriptType(int(caseScriptType))
            # THERE IS ONLY ONE LEVEL WHERE A STRING IS USED ISTEAD OF AN INT; TODO: MAKE THIS PRETTIER
            inverted = (
                not bool(int(inverted)) if inverted != 'false' else True
            )   # 'false' IS int(0) SO not bool(int(0)) == True
            actor = (
                HLDType(actor)
                if actor not in {'-1', '0', '1', '-999999'}
                else actor
            )  # type: HLDType | Literal['-1','0','1','-999999']
            delay = int(delay)
        return cls(
            depends_on=depends_on,
            casescript=caseScriptType,
            inverted=inverted,
            actor=actor,
            delay=delay,
        )

    def to_string(self) -> str:
        left_part = (
            f'{len(self.depends_on)},{",".join([str(uid) for uid in self.depends_on])}'
            if len(self.depends_on)
            else '-999999'
        )
        if self.casescript == CaseScriptType.NO:
            return left_part
        else:
            right_part = f'{self.casescript.value},{int(not self.inverted)},{self.actor},{self.delay}'
            return f'{left_part},caseScript,{right_part}'

    def __eq__(self, other) -> bool:
        if other.__class__ is not self.__class__:
            return False
        return self.__dict__ == other.__dict__


class HLDObj:
    """
    A python representation of a HLD object.
    """

    def __init__(
        self,
        type: HLDType,
        x: int,
        y: int,
        uid: int,
        attrs: dict[str, int | float | str],
        dependencies: Dependencies,
        layer: int = 0,
    ) -> None:
        self.type = type
        self.x = x
        self.y = y
        self.uid = uid
        self.attrs = attrs
        self.dependencies = dependencies
        self.layer = layer

    @classmethod
    def from_string(cls, line: str):
        """
        Creates an HLD object from a string as they are formated in level files.

        obj,Spawner,593,536,352,6,-999999,++,-1=dirk,-2=-999999,-4=1,-5=0,-6=-1,-7=0,-8=0,
        """
        regex_match = re.match(
            r'obj,(?P<type>.*?),(?P<uid>.*?),(?P<x>.*?),(?P<y>.*?),(?P<layer>.*?),(?P<dependencies>.*?),\+\+,(?P<attrs>.*)',
            line.strip().replace('//', ''),
        )
        if not regex_match:
            raise HLDError(f'This line is not an HLDObject: {line}')
        type = regex_match.group('type')
        uid = int(regex_match.group('uid'))
        x = int(regex_match.group('x'))
        y = int(regex_match.group('y'))
        layer = int(regex_match.group('layer'))
        dependencies = Dependencies.from_string(
            regex_match.group('dependencies')
        )
        attrs = {
            pair.split('=')[0]: _int_float_str_convert(pair.split('=')[1])
            for pair in regex_match.group('attrs').split(',')
            if '=' in pair
        }
        return cls(
            type=HLDType(type),
            x=x,
            y=y,
            uid=uid,
            layer=layer,
            dependencies=dependencies,
            attrs=attrs,
        )

    def to_string(self) -> str:
        """
        Gets the object in a string form as they are formated in level files.
        """
        attrs_to_str = ','.join(
            [f'{key}={value}' for key, value in self.attrs.items()]
        )
        return f'\n\t //obj,{self.type},{self.uid},{self.x},{self.y},{self.layer},{self.dependencies.to_string()},++,{attrs_to_str},'

    def __eq__(self, other) -> bool:
        if other.__class__ is not self.__class__:
            return False
        return self.__dict__ == other.__dict__


def _int_float_str_convert(val: str) -> int | float | str:
    try:
        return int(val)
    except:
        pass
    try:
        return float(val)
    except:
        pass
    return val
