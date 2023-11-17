import json
from base64 import standard_b64decode, standard_b64encode
from dataclasses import dataclass, fields
from typing import Iterable

from hldlib.aliases import StrPath


# lists and dicts in savefile data always have a training separator
# which we have to add if len(...) > 0
def trail_join(separator: str, input: Iterable[str]):
    return separator.join(input) + separator * bool(input)


# lists and dicts in savefile data always have a training separator
# which we have to remove before splitting
def untrail_split(separator: str, input: str) -> list[str]:
    # if we dont want to return [''] on empty string
    if not input:
        return []
    return input.removesuffix(separator).split(separator)


def string_to_header_body(string: str) -> tuple[str, dict]:
    # the first 80 characters are machine specific header
    header, body_str = string[:80], string[80:]
    # we have to remove last character after decoding
    decoded = standard_b64decode(body_str)[:-1]
    body = json.loads(decoded)
    return header, body


def header_body_to_string(header: str, body: dict) -> str:
    body_str = json.dumps(body, indent=0)
    # we are adding back the last character we removed while decoding
    encoded = str(standard_b64encode(bytes(body_str + '\x00', 'utf8')), 'utf8')
    return header + encoded


def data_to_list(string: str) -> list[str]:
    return untrail_split('+', string)


def list_to_data(list_: list) -> str:
    return trail_join('+', list_)


def data_to_dict(string: str) -> dict[str, list[str]]:
    keqvs = untrail_split('>', string)
    return {
        k: untrail_split('&', v)
        for k, v in [keqv.split('=') for keqv in keqvs]
    }


def dict_to_data(dict_: dict) -> str:
    return trail_join(
        '>', [k + '=' + trail_join('&', v) for k, v in dict_.items()]
    )


@dataclass
class Savefile:
    badass: float
    mapMod: dict[str, list[str]]
    dateTime: float
    healthUp: float
    cl: dict[str, list[str]]
    destruct: dict[str, list[str]]
    values: dict[str, list[str]]
    gunReminderTimes: float
    fireplaceSave: float
    checkHP: float
    compShell: float
    cSwords: list[str]
    cape: float
    halluc: float
    newcomerHoardeMessageShown: float
    tutHeal: float
    noSpawn: list[str]
    checkY: float
    specialUp: float
    checkBat: float
    noviceMode: float
    successfulHealTimes: float
    cCapes: list[str]
    CH: float
    gear: float
    checkCID: float
    rooms: list[str]
    permaS: dict[str, list[str]]
    checkRoom: float
    wellMap: list[str]
    cShells: list[str]
    eq01: float
    tablet: list[str]
    successfulWarpTimes: float
    skill: list[str]
    bosses: dict[str, list[str]]
    scK: dict[str, list[str]]
    warp: list[str]
    hasMap: float
    events: list[str]
    gearReminderTimes: float
    enemies: dict[str, list[str]]
    scUp: list[str]
    checkX: float
    bossGearbits: list[str]
    cues: list[str]
    playT: float
    well: list[str]
    sc: list[str]
    drifterkey: float
    successfulCollectTimes: float
    checkAmmo: float
    checkStash: float
    charDeaths: float
    eq00: float
    healthKits: list[str]
    sword: float
    gameName: str

    header: str

    @classmethod
    def loads(cls, string: str):
        header, body = string_to_header_body(string)

        # if a weapon is not equipped there is no 'eq0X' in savefile data
        # which we need so we represent an empty slot with a meaningless 0.0
        # that we are going to remove on dump
        if 'eq00' not in body:
            body['eq00'] = 0.0
        if 'eq01' not in body:
            body['eq01'] = 0.0
        body['header'] = header

        for field in fields(cls):
            print(field.type)
            if field.type == list[str]:
                body[field.name] = data_to_list(body[field.name])
            if field.type == dict[str, list[str]]:
                body[field.name] = data_to_dict(body[field.name])

        return cls(**body)

    @classmethod
    def load(cls, path: StrPath):
        with open(path, 'r') as f:
            return cls.loads(f.read())

    def dumps(self) -> str:
        body = self.__dict__.copy()

        # 'eq0X' == 0.0 is a representation of an empty slot
        # so we have to remove them before dumping
        if body['eq00'] == 0.0:
            body.pop('eq00')
        if body['eq01'] == 0.0:
            body.pop('eq01')
        header = body.pop('header')

        for k, v in body.items():
            if isinstance(v, list):
                body[k] = list_to_data(v)
            if isinstance(v, dict):
                body[k] = dict_to_data(v)

        return header_body_to_string(header, body)

    def dump(self, path: StrPath):
        with open(path, 'w') as f:
            f.write(self.dumps())
