import sys
from dataclasses import dataclass
from enum import Enum
from typing import NamedTuple, TextIO

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
                sys.stderr.write(f'broken object loaded: {err!r}')
                sys.stderr.write('\n')

        return cls(level_name, date, objects, settings, layers)

    @classmethod
    def load(cls, f: TextIO, level_name: str):
        return cls.loads(f.read(), level_name)


class LevelInfo(NamedTuple):
    id: int
    real_name: str

    @property
    def os_name(self) -> str:
        if sys.platform == 'win32':
            return self.real_name
        else:
            return self.real_name.lower()


class LevelName(LevelInfo, Enum):
    """
    All vanilla HLD level names and ids.
    """

    IN_01_BROKENSHALLOWS = 46, 'rm_IN_01_brokenshallows'
    IN_02_TUTORIAL = 47, 'rm_IN_02_Tutorial'
    IN_03_TUT_COMBAT = 48, 'rm_IN_03_Tut_Combat'
    IN_HORIZONCLIFF = 49, 'rm_IN_HorizonCliff'
    IN_HALUCINATIONDEATH = 50, 'rm_IN_HalucinationDeath'
    IN_DRIFTERFIRE = 51, 'rm_IN_Drifterfire'
    IN_BLACKWAITROOM = 52, 'rm_IN_BlackWaitRoom'
    IN_BACKERTABLET = 53, 'rm_IN_BackerTablet'
    INL_SECRETS = 55, 'rm_INL_Secrets'
    LIN_GAPS = 56, 'rm_LIN_Gaps'
    LIN_COMBAT = 57, 'rm_LIN_Combat'
    C_DRIFTERWORKSHOP = 60, 'rm_C_DrifterWorkshop'
    C_CENTRAL = 61, 'rm_C_Central'
    C_DREGS_N = 62, 'rm_C_Dregs_N'
    C_DREGS_S = 63, 'rm_C_Dregs_S'
    C_DREGS_E = 64, 'rm_C_Dregs_E'
    C_DREGS_W = 65, 'rm_C_Dregs_W'
    C_VEN_APOTH = 66, 'rm_C_Ven_Apoth'
    C_VEN_DASH = 67, 'rm_C_Ven_Dash'
    C_VEN_GUN = 68, 'rm_C_Ven_Gun'
    C_VEN_SPEC = 69, 'rm_C_Ven_Spec'
    C_VEN_SDOJO = 70, 'rm_C_Ven_SDojo'
    CARENA = 71, 'rm_CArena'
    PAX_STAGING = 72, 'rm_PAX_Staging'
    PAX_ARENA1 = 73, 'rm_PAX_arena1'
    PAX_ARENA2 = 74, 'rm_PAX_arena2'
    PAX_ARENAE = 75, 'rm_PAX_arenaE'
    PAX_ARENAW = 76, 'rm_PAX_arenaW'
    PAX_ARENAALL = 77, 'rm_PAX_arenaAll'
    C_BACKERTABLETX = 78, 'rm_C_BackerTabletX'
    TELEVATORSHAFT = 79, 'rm_TelevatorShaft'
    NL_ENTRANCEPATH = 84, 'rm_NL_EntrancePath'
    NX_TITANVISTA = 85, 'rm_NX_TitanVista'
    NX_NORTHHALL = 86, 'rm_NX_NorthHall'
    NL_CAVEVAULT = 87, 'rm_NL_CaveVAULT'
    NX_AFTERTITAN = 88, 'rm_NX_AfterTitan'
    NC_NPCHATCHERY = 89, 'rm_NC_NPCHatchery'
    NX_SHRINEPATH = 90, 'rm_NX_ShrinePath'
    NL_SHRINEPATH2VAULT = 91, 'rm_NL_ShrinePath2VAULT'
    NX_CAVE01 = 92, 'rm_NX_Cave01'
    NX_SHRINEPATH_2 = 93, 'rm_NX_ShrinePath_2'
    NX_MOONCOURTYARD = 94, 'rm_NX_MoonCourtyard'
    NX_TOWERLOCK = 95, 'rm_NX_TowerLock'
    NC_CLIFFCAMPFIRE = 96, 'rm_NC_CliffCampfire'
    NL_TOBROKENSHALLOWS = 97, 'rm_NL_ToBrokenShallows'
    NX_STAIRS03 = 98, 'rm_NX_Stairs03'
    NL_WARPROOM = 100, 'rm_NL_WarpRoom'
    NL_CRUSHWARPHALL = 101, 'rm_NL_CrushWarpHall'
    NL_CRUSHTRANSITION = 102, 'rm_NL_CrushTransition'
    NL_CRUSHBACKLOOP = 103, 'rm_NL_CrushBackLoop'
    NC_CRUSHARENA = 104, 'rm_NC_CrushArena'
    NL_DROPSPIRALOPEN = 106, 'rm_NL_DropSpiralOpen'
    NL_DROPPITS = 107, 'rm_NL_DropPits'
    NL_DROPBLOCKCULTFIGHT = 108, 'rm_NL_DropBlockCultFight'
    NL_DROPARENA = 109, 'rm_NL_DropArena'
    NL_GAPOPENING = 111, 'rm_NL_GapOpening'
    NX_GAPWIDE = 112, 'rm_NX_GapWide'
    NL_GAPHALLWAY = 113, 'rm_NL_GapHallway'
    NL_RISINGARENA = 114, 'rm_NL_RisingArena'
    NX_CATHEDRALENTRANCE = 116, 'rm_NX_CathedralEntrance'
    NX_CATHEDRALHALL = 117, 'rm_NX_CathedralHall'
    NL_ALTARTHRONE = 118, 'rm_NL_AltarThrone'
    NX_SPIRALSTAIRCASE = 119, 'rm_NX_SpiralStaircase'
    NX_LIBRARIANTABLET = 120, 'rm_NX_LibrarianTablet'
    NX_JERKPOPE = 121, 'rm_NX_JerkPope'
    NL_STAIRASCENT = 123, 'rm_NL_StairAscent'
    NL_CRUSHARENA = 124, 'rm_NL_CrushArena'
    SX_SOUTHOPENING = 128, 'rm_SX_SouthOpening'
    CH_CTEMPLATE = 129, 'rm_CH_CTemplate'
    SX_TOWERSOUTH = 130, 'rm_SX_TowerSouth'
    SX_NPC = 131, 'rm_SX_NPC'
    S_GAUNTLET_ELEVATOR = 132, 'rm_S_Gauntlet_Elevator'
    CH_BGUNPILLARS = 133, 'rm_CH_BGunPillars'
    CH_BFINAL = 134, 'rm_CH_BFinal'
    S_GAUNTLETEND = 135, 'rm_S_GauntletEnd'
    CH_BDIRKDEMOLITION = 137, 'rm_CH_BDirkDemolition'
    CH_TABIGONE = 139, 'rm_CH_TABigOne'
    CH_CGATEBLOCK = 140, 'rm_CH_CGateBlock'
    CH_BMADDASH = 141, 'rm_CH_BMadDash'
    CH_TLONGESTROAD = 142, 'rm_CH_TLongestRoad'
    S_BULLETBAKER = 143, 'rm_S_BulletBaker'
    CH_CENDHALL = 144, 'rm_CH_CEndHall'
    CH_CTURNHALL = 146, 'rm_CH_CTurnHall'
    CH_BFPS = 147, 'rm_CH_Bfps'
    CH_CBIGGGNS = 148, 'rm_CH_CBigggns'
    CH_CSPAWNGROUND = 149, 'rm_CH_CSpawnGround'
    S_COUNTACULARD = 150, 'rm_S_CountAculard'
    CH_ACORNER = 152, 'rm_CH_ACorner'
    CH_BDIRKDELUGE = 154, 'rm_CH_BDirkDeluge'
    CH_BPODS = 155, 'rm_CH_BPods'
    CH_BGUNDIRKDASH = 156, 'rm_CH_BGunDirkDash'
    S_MARKSCYTHE = 157, 'rm_S_MarkScythe'
    S_GAUNTLETLINKUP = 158, 'rm_S_GauntletLinkup'
    CH_APILLARBIRD = 160, 'rm_CH_APillarBird'
    CH_CSPIRAL = 161, 'rm_CH_CSpiral'
    CH_TBIRDSTANDOFF = 162, 'rm_CH_TBirdStandoff'
    CH_BLEAPERFALL = 163, 'rm_CH_BLeaperFall'
    S_BENNYARROW = 164, 'rm_S_BennyArrow'
    S_GAUNTLETTITANFINALE = 165, 'rm_S_GauntletTitanFinale'
    EA_EASTOPENING = 171, 'rm_EA_EastOpening'
    EC_SWORDBRIDGE = 172, 'rm_EC_SwordBridge'
    EL_FLAMEELEVATORENTER = 173, 'rm_EL_FlameElevatorEnter'
    EA_WATERTUNNELLAB = 174, 'rm_EA_WaterTunnelLAB'
    EC_THEPLAZA = 175, 'rm_EC_ThePlaza'
    EC_NPCDRUGDEN = 176, 'rm_EC_NPCDrugDen'
    EX_TOWEREAST = 177, 'rm_EX_TowerEast'
    EB_BOGSTREET = 178, 'rm_EB_BogStreet'
    EC_PLAZATOLOOP = 179, 'rm_EC_PlazaToLoop'
    EL_MEGAHUGELAB = 181, 'rm_EL_MegaHugeLAB'
    EB_MELTYMASHARENA = 182, 'rm_EB_MeltyMashArena'
    EB_FLAMEPITLAB = 183, 'rm_EB_FlamePitLAB'
    EL_FLAMEELEVATOREXIT = 184, 'rm_EL_FlameElevatorExit'
    EB_DEADOTTERWALK = 185, 'rm_EB_DeadOtterWalk'
    EC_PLAZAACCESSLAB = 187, 'rm_EC_PlazaAccessLAB'
    EC_DOCKSLAB = 188, 'rm_EC_DocksLab'
    EX_DOCKSCAMPFIRE = 189, 'rm_EX_DocksCampfire'
    EV_DOCKSBRIDGE = 190, 'rm_EV_DocksBridge'
    EL_FROGARENA = 191, 'rm_EL_FrogArena'
    EC_BIGBOGLAB = 193, 'rm_EC_BigBogLAB'
    EA_BOGTEMPLECAMP = 194, 'rm_EA_BogTempleCamp'
    EA_FROGBOSS = 195, 'rm_EA_FrogBoss'
    EC_TEMPLEISHVAULT = 196, 'rm_EC_TempleIshVault'
    EC_EASTLOOP = 198, 'rm_EC_EastLoop'
    EC_LOOPLAB = 199, 'rm_EC_LoopLAB'
    EB_MELTYLEAPERARENA = 200, 'rm_EB_MeltyLeaperArena'
    EC_PLAZATODOCKS = 202, 'rm_EC_PlazaToDocks'
    EA_DOCKFIGHTLAB = 203, 'rm_EA_DockFightLab'
    EB_UNDEROTTERBIGRIFLERUMBLE = 204, 'rm_EB_UnderOtterBigRifleRumble'
    EB_CLEANERSHOLE = 205, 'rm_EB_CleanersHole'
    WA_ENTRANCE = 209, 'rm_WA_Entrance'
    WL_PRISONHALVAULT = 210, 'rm_WL_PrisonHALVAULT'
    WA_DEADWOOD = 211, 'rm_WA_Deadwood'
    WA_DEADWOODS1 = 212, 'rm_WA_DeadwoodS1'
    WA_GROTTO_BUFFINTRO = 213, 'rm_WA_Grotto_buffIntro'
    WC_WINDINGWOOD = 214, 'rm_WC_WindingWood'
    WC_GROTTONPC = 215, 'rm_WC_GrottoNPC'
    WL_NPCTREEHOUSE = 216, 'rm_WL_NPCTreehouse'
    WC_MINILAB = 217, 'rm_WC_MiniLab'
    WT_THEWOOD = 218, 'rm_WT_TheWood'
    WA_ENTSWITCH = 219, 'rm_WA_EntSwitch'
    WC_MEADOWOODCORNER = 220, 'rm_WC_MeadowoodCorner'
    WB_TREETREACHERY = 222, 'rm_WB_TreeTreachery'
    WL_WESTDRIFTERVAULT = 223, 'rm_WL_WestDrifterVault'
    WT_SLOWLAB = 225, 'rm_WT_SlowLab'
    WC_CLIFFSIDECELLSREDUX = 226, 'rm_WC_CliffsideCellsRedux'
    WC_PRISONHAL = 227, 'rm_WC_PrisonHAL'
    WC_THINFOREST = 229, 'rm_WC_ThinForest'
    WC_SIMPLEPATH = 230, 'rm_WC_SimplePath'
    WC_CRYSTALLAKE = 231, 'rm_WC_CrystalLake'
    WC_CRYSTALLAKEVAULT = 232, 'rm_WC_CrystalLakeVault'
    WC_PRISONHALLEND = 233, 'rm_WC_PrisonHallEnd'
    WC_THINFORESTLOW = 234, 'rm_WC_ThinForestLow'
    WC_THINFORESTLOWSECRET = 235, 'rm_WC_ThinForestLowSecret'
    WA_TITANFALLS = 236, 'rm_WA_TitanFalls'
    WA_VALE = 238, 'rm_WA_Vale'
    WC_BIGMEADOW = 239, 'rm_WC_BigMeadow'
    WC_BIGMEADOWVAULT = 240, 'rm_WC_BigMeadowVAULT'
    WC_MEADOWCAVECROSSING = 241, 'rm_WC_MeadowCaveCrossing'
    WB_BIGBATTLE = 242, 'rm_WB_BigBattle'
    WB_TANUKITROUBLE = 243, 'rm_WB_TanukiTrouble'
    WC_RUINCLEARING = 244, 'rm_WC_RuinClearing'
    WX_BOSS = 245, 'rm_WX_Boss'
    WA_TOWERENTER = 246, 'rm_WA_TowerEnter'
    WA_MULTIENTRANCELAB = 247, 'rm_WA_MultiEntranceLab'
    WA_CRSYTALDESCENT = 248, 'rm_WA_CrsytalDescent'
    WA_GROTTOX = 250, 'rm_WA_GrottoX'
    WB_CRYSTALQUEEN = 251, 'rm_WB_CrystalQueen'
    WT_PROTOGRID = 252, 'rm_WT_ProtoGrid'
    WV_PUZZLEPALACENEW = 253, 'rm_WV_PuzzlePalaceNEW'
    A_ELEVATORSHAFTUPPER = 256, 'rm_A_ElevatorShaftUpper'
    A_ELEVATORSHAFT = 257, 'rm_A_ElevatorShaft'
    A_PREDOWNWARD = 258, 'rm_A_PreDownward'
    A_DOWNWARD = 259, 'rm_A_Downward'
    A_DOWNWARDDEAD = 260, 'rm_A_DownwardDead'
    A_DOWNWARDDEADREVISIT = 261, 'rm_A_DownwardDeadRevisit'
    A_EMBERROOM = 262, 'rm_A_EmberRoom'
    BOSSRUSH_HUB = 265, 'rm_BossRush_Hub'
    BOSSRUSH_FROGBOSS = 266, 'rm_BossRush_FrogBoss'
    BOSSRUSH_JERKPOPE = 267, 'rm_BossRush_JerkPope'
    BOSSRUSH_GENERAL = 268, 'rm_BossRush_General'
    BOSSRUSH_BULLETBAKER = 269, 'rm_BossRush_BulletBaker'
    BOSSRUSH_COUNTACULARD = 270, 'rm_BossRush_CountAculard'
    BOSSRUSH_MARKSCYTHE = 271, 'rm_BossRush_MarkScythe'
    BOSSRUSH_BENNYARROW = 272, 'rm_BossRush_BennyArrow'
    BOSSRUSH_EMBER = 273, 'rm_BossRush_Ember'

    @classmethod
    def from_id(cls, id_: int) -> 'LevelName | None':
        for info in cls:
            if info.id == id_:
                return info

    @classmethod
    def from_name(cls, name: str) -> 'LevelName | None':
        for info in cls:
            if info.real_name.lower() == name.lower():
                return info
