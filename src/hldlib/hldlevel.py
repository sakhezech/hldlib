import os
import re
from enum import Enum
from pathlib import Path

from hldlib.hlddirections import HLDDirection
from hldlib.hlderror import HLDError
from hldlib.hldobjects import HLDObj, _int_float_str_convert


class HLDLevel:
    """
    A python representation of a HLD level.
    """

    def __init__(
        self,
        name: str,
        date: float,
        layer_names: dict,
        room_settings: dict,
        objects: list[HLDObj],
        direction: HLDDirection,
    ) -> None:
        self.name = name
        self.date = date
        self.layer_names = layer_names
        self.room_settings = room_settings
        self.objects = objects
        self.direction = direction

    @classmethod
    def load(
        cls, path: str | Path, direction: HLDDirection = HLDDirection.NONE
    ):
        """
        Loads a level from path.
        """
        name = os.path.basename(path)
        with open(path, 'r') as f:
            return cls.from_string(f.read(), name, direction)

    @classmethod
    def from_string(cls, string: str, name: str, direction: HLDDirection):
        """
        Loads a level from a string.
        """
        lines = string.split('\n')
        layer_names = {}
        room_settings = {}
        objects = []
        i = 0
        # fmt: off
        # TODO: this is impossible to read
        while not (match := re.match(r"(?:DATE|VERSION),(?P<date>.*?),", lines[i])):
            i += 1
        date = float(match.group("date"))
        i += 1
        while not (match := re.search(r"layerName,(?P<id>.*?),(?P<name>.*?),", lines[i])):
            i += 1
        while (match := re.search(r"layerName,(?P<id>.*?),(?P<name>.*?),", lines[i])):
            layer_names[int(match.group("id"))] = match.group("name")
            i += 1
        while not (match := re.search(r",floorSpr,", lines[i])):
            i += 1
        split_line = list(map(_int_float_str_convert,
                          lines[i].lstrip().split(",")[:-1]))
        sketch = split_line[-4:]
        rest_of_settings = iter(split_line[:-4])
        for x in rest_of_settings:
            room_settings[x] = next(rest_of_settings)
        room_settings[sketch[0]] = [sketch[1], sketch[2], sketch[3]]
        i += 1
        for line in lines[i:]:
            if re.search(r"obj,.*?,.*?,", line):
                objects.append(HLDObj.from_string(line))
        # fmt: on

        return cls(
            date=date,
            layer_names=layer_names,
            room_settings=room_settings,
            objects=objects,
            name=name,
            direction=direction,
        )

    def dump(self, path: str | Path) -> None:
        """
        Dumps the level to path. Uses levels name as the dumped file name.
        """
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, self.name), 'w') as file:
            file.write(self.to_string())

    def to_string(self) -> str:
        """
        Gets the level in a string form. Can be used to write to a file.
        """
        return (
            f'DATE,{self.date},'
            + '\n\t '
            + '\n\t '.join(
                [
                    f'layerName,{key},{value},'
                    for key, value in self.layer_names.items()
                ]
            )
            + '\n\t '
            + ','.join(
                [
                    f'{key},{value}'
                    for key, value in self.room_settings.items()
                    if key != 'sketchalpha'
                ]
            )
            + f",sketchalpha,{','.join(list(map(str, self.room_settings['sketchalpha'])))},"
            + ''.join([obj.to_string() for obj in self.objects])
        )

    def __eq__(self, other) -> bool:
        if other.__class__ is not self.__class__:
            return False
        return self.__dict__ == other.__dict__


class HLDLevelNames(Enum):
    IN_01_BROKENSHALLOWS = 46
    IN_02_TUTORIAL = 47
    IN_03_TUT_COMBAT = 48
    IN_HORIZONCLIFF = 49
    IN_HALUCINATIONDEATH = 50
    IN_DRIFTERFIRE = 51
    IN_BLACKWAITROOM = 52
    IN_BACKERTABLET = 53
    INL_SECRETS = 55
    LIN_GAPS = 56
    LIN_COMBAT = 57
    C_DRIFTERWORKSHOP = 60
    C_CENTRAL = 61
    C_DREGS_N = 62
    C_DREGS_S = 63
    C_DREGS_E = 64
    C_DREGS_W = 65
    C_VEN_APOTH = 66
    C_VEN_DASH = 67
    C_VEN_GUN = 68
    C_VEN_SPEC = 69
    C_VEN_SDOJO = 70
    CARENA = 71
    PAX_STAGING = 72
    PAX_ARENA1 = 73
    PAX_ARENA2 = 74
    PAX_ARENAE = 75
    PAX_ARENAW = 76
    PAX_ARENAALL = 77
    C_BACKERTABLETX = 78
    TELEVATORSHAFT = 79
    NL_ENTRANCEPATH = 84
    NX_TITANVISTA = 85
    NX_NORTHHALL = 86
    NL_CAVEVAULT = 87
    NX_AFTERTITAN = 88
    NC_NPCHATCHERY = 89
    NX_SHRINEPATH = 90
    NL_SHRINEPATH2VAULT = 91
    NX_CAVE01 = 92
    NX_SHRINEPATH_2 = 93
    NX_MOONCOURTYARD = 94
    NX_TOWERLOCK = 95
    NC_CLIFFCAMPFIRE = 96
    NL_TOBROKENSHALLOWS = 97
    NX_STAIRS03 = 98
    NL_WARPROOM = 100
    NL_CRUSHWARPHALL = 101
    NL_CRUSHTRANSITION = 102
    NL_CRUSHBACKLOOP = 103
    NC_CRUSHARENA = 104
    NL_DROPSPIRALOPEN = 106
    NL_DROPPITS = 107
    NL_DROPBLOCKCULTFIGHT = 108
    NL_DROPARENA = 109
    NL_GAPOPENING = 111
    NX_GAPWIDE = 112
    NL_GAPHALLWAY = 113
    NL_RISINGARENA = 114
    NX_CATHEDRALENTRANCE = 116
    NX_CATHEDRALHALL = 117
    NL_ALTARTHRONE = 118
    NX_SPIRALSTAIRCASE = 119
    NX_LIBRARIANTABLET = 120
    NX_JERKPOPE = 121
    NL_STAIRASCENT = 123
    NL_CRUSHARENA = 124
    SX_SOUTHOPENING = 128
    CH_CTEMPLATE = 129
    SX_TOWERSOUTH = 130
    SX_NPC = 131
    S_GAUNTLET_ELEVATOR = 132
    CH_BGUNPILLARS = 133
    CH_BFINAL = 134
    S_GAUNTLETEND = 135
    CH_BDIRKDEMOLITION = 137
    CH_TABIGONE = 139
    CH_CGATEBLOCK = 140
    CH_BMADDASH = 141
    CH_TLONGESTROAD = 142
    S_BULLETBAKER = 143
    CH_CENDHALL = 144
    CH_CTURNHALL = 146
    CH_BFPS = 147
    CH_CBIGGGNS = 148
    CH_CSPAWNGROUND = 149
    S_COUNTACULARD = 150
    CH_ACORNER = 152
    CH_BDIRKDELUGE = 154
    CH_BPODS = 155
    CH_BGUNDIRKDASH = 156
    S_MARKSCYTHE = 157
    S_GAUNTLETLINKUP = 158
    CH_APILLARBIRD = 160
    CH_CSPIRAL = 161
    CH_TBIRDSTANDOFF = 162
    CH_BLEAPERFALL = 163
    S_BENNYARROW = 164
    S_GAUNTLETTITANFINALE = 165
    EA_EASTOPENING = 171
    EC_SWORDBRIDGE = 172
    EL_FLAMEELEVATORENTER = 173
    EA_WATERTUNNELLAB = 174
    EC_THEPLAZA = 175
    EC_NPCDRUGDEN = 176
    EX_TOWEREAST = 177
    EB_BOGSTREET = 178
    EC_PLAZATOLOOP = 179
    EL_MEGAHUGELAB = 181
    EB_MELTYMASHARENA = 182
    EB_FLAMEPITLAB = 183
    EL_FLAMEELEVATOREXIT = 184
    EB_DEADOTTERWALK = 185
    EC_PLAZAACCESSLAB = 187
    EC_DOCKSLAB = 188
    EX_DOCKSCAMPFIRE = 189
    EV_DOCKSBRIDGE = 190
    EL_FROGARENA = 191
    EC_BIGBOGLAB = 193
    EA_BOGTEMPLECAMP = 194
    EA_FROGBOSS = 195
    EC_TEMPLEISHVAULT = 196
    EC_EASTLOOP = 198
    EC_LOOPLAB = 199
    EB_MELTYLEAPERARENA = 200
    EC_PLAZATODOCKS = 202
    EA_DOCKFIGHTLAB = 203
    EB_UNDEROTTERBIGRIFLERUMBLE = 204
    EB_CLEANERSHOLE = 205
    WA_ENTRANCE = 209
    WL_PRISONHALVAULT = 210
    WA_DEADWOOD = 211
    WA_DEADWOODS1 = 212
    WA_GROTTO_BUFFINTRO = 213
    WC_WINDINGWOOD = 214
    WC_GROTTONPC = 215
    WL_NPCTREEHOUSE = 216
    WC_MINILAB = 217
    WT_THEWOOD = 218
    WA_ENTSWITCH = 219
    WC_MEADOWOODCORNER = 220
    WB_TREETREACHERY = 222
    WL_WESTDRIFTERVAULT = 223
    WT_SLOWLAB = 225
    WC_CLIFFSIDECELLSREDUX = 226
    WC_PRISONHAL = 227
    WC_THINFOREST = 229
    WC_SIMPLEPATH = 230
    WC_CRYSTALLAKE = 231
    WC_CRYSTALLAKEVAULT = 232
    WC_PRISONHALLEND = 233
    WC_THINFORESTLOW = 234
    WC_THINFORESTLOWSECRET = 235
    WA_TITANFALLS = 236
    WA_VALE = 238
    WC_BIGMEADOW = 239
    WC_BIGMEADOWVAULT = 240
    WC_MEADOWCAVECROSSING = 241
    WB_BIGBATTLE = 242
    WB_TANUKITROUBLE = 243
    WC_RUINCLEARING = 244
    WX_BOSS = 245
    WA_TOWERENTER = 246
    WA_MULTIENTRANCELAB = 247
    WA_CRSYTALDESCENT = 248
    WA_GROTTOX = 250
    WB_CRYSTALQUEEN = 251
    WT_PROTOGRID = 252
    WV_PUZZLEPALACENEW = 253
    A_ELEVATORSHAFTUPPER = 256
    A_ELEVATORSHAFT = 257
    A_PREDOWNWARD = 258
    A_DOWNWARD = 259
    A_DOWNWARDDEAD = 260
    A_DOWNWARDDEADREVISIT = 261
    A_EMBERROOM = 262
    BOSSRUSH_HUB = 265
    BOSSRUSH_FROGBOSS = 266
    BOSSRUSH_JERKPOPE = 267
    BOSSRUSH_GENERAL = 268
    BOSSRUSH_BULLETBAKER = 269
    BOSSRUSH_COUNTACULARD = 270
    BOSSRUSH_MARKSCYTHE = 271
    BOSSRUSH_BENNYARROW = 272
    BOSSRUSH_EMBER = 273


def get_id_from_name(name: str) -> int:
    """
    A way to convert level name to its internal ID.
    Not case sensitive.
    """
    try:
        return HLDLevelNames[
            name.removeprefix('rm_').removesuffix('.lvl').upper()
        ].value
    except KeyError:
        raise HLDError(f'No such level named {name}.')


def get_name_from_id(id_: int) -> str:
    """
    A way to convert internal level ID to its name.
    Returns in lowercase.
    """
    try:
        return f'rm_{HLDLevelNames(id_).name.lower()}.lvl'
    except ValueError:
        raise HLDError(f'No such level with id {id_}.')
