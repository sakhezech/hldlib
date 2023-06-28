import os
from pathlib import Path
import re
from hldlib.hldobjects import HLDObj, _int_float_str_convert
from hldlib.hlddirections import HLDDirection
from hldlib.hlderror import HLDError


class HLDLevel:
    """
    A python representation of a HLD level.
    """

    def __init__(self, name: str, date: float, layer_names: dict, room_settings: dict, objects: list[HLDObj], direction: HLDDirection) -> None:
        self.name = name
        self.date = date
        self.layer_names = layer_names
        self.room_settings = room_settings
        self.objects = objects
        self.direction = direction

    @classmethod
    def load(cls, path: str | Path, direction: HLDDirection = HLDDirection.NONE):
        """
        Loads a level from path.
        """
        name = os.path.basename(path)
        with open(path, "r") as f:
            return cls.from_string(f.read(), name, direction)

    @classmethod
    def from_string(cls, string: str, name: str, direction: HLDDirection):
        """
        Loads a level from a string.
        """
        lines = string.split("\n")
        layer_names = {}
        room_settings = {}
        objects = []
        i = 0

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

        return cls(date=date, layer_names=layer_names, room_settings=room_settings, objects=objects, name=name, direction=direction)

    def dump(self, path: str | Path) -> None:
        """
        Dumps the level to path. Uses levels name as the dumped file name.
        """
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, self.name), "w") as file:
            file.write(self.to_string())

    def to_string(self) -> str:
        """
        Gets the level in a string form. Can be used to write to a file.
        """
        return f"DATE,{self.date}," +\
            "\n\t " + "\n\t ".join([f"layerName,{key},{value}," for key, value in self.layer_names.items()]) +\
            "\n\t " + ",".join([f"{key},{value}" for key, value in self.room_settings.items() if key != "sketchalpha"]) +\
            f",sketchalpha,{','.join(list(map(str, self.room_settings['sketchalpha'])))}," +\
            "".join([obj.to_string() for obj in self.objects])

    def __eq__(self, other) -> bool:
        if other.__class__ is not self.__class__:
            return False
        return self.__dict__ == other.__dict__


level_names_and_ids: set[tuple[str, int]] = {
    ("rm_in_01_brokenshallows.lvl", 46),
    ("rm_in_02_tutorial.lvl", 47),
    ("rm_in_03_tut_combat.lvl", 48),
    ("rm_in_horizoncliff.lvl", 49),
    ("rm_in_halucinationdeath.lvl", 50),
    ("rm_in_drifterfire.lvl", 51),
    ("rm_in_blackwaitroom.lvl", 52),
    ("rm_in_backertablet.lvl", 53),
    ("rm_inl_secrets.lvl", 55),
    ("rm_lin_gaps.lvl", 56),
    ("rm_lin_combat.lvl", 57),
    ("rm_c_drifterworkshop.lvl", 60),
    ("rm_c_central.lvl", 61),
    ("rm_c_dregs_n.lvl", 62),
    ("rm_c_dregs_s.lvl", 63),
    ("rm_c_dregs_e.lvl", 64),
    ("rm_c_dregs_w.lvl", 65),
    ("rm_c_ven_apoth.lvl", 66),
    ("rm_c_ven_dash.lvl", 67),
    ("rm_c_ven_gun.lvl", 68),
    ("rm_c_ven_spec.lvl", 69),
    ("rm_c_ven_sdojo.lvl", 70),
    ("rm_carena.lvl", 71),
    ("rm_pax_staging.lvl", 72),
    ("rm_pax_arena1.lvl", 73),
    ("rm_pax_arena2.lvl", 74),
    ("rm_pax_arenae.lvl", 75),
    ("rm_pax_arenaw.lvl", 76),
    ("rm_pax_arenaall.lvl", 77),
    ("rm_c_backertabletx.lvl", 78),
    ("rm_televatorshaft.lvl", 79),
    ("rm_nl_entrancepath.lvl", 84),
    ("rm_nx_titanvista.lvl", 85),
    ("rm_nx_northhall.lvl", 86),
    ("rm_nl_cavevault.lvl", 87),
    ("rm_nx_aftertitan.lvl", 88),
    ("rm_nc_npchatchery.lvl", 89),
    ("rm_nx_shrinepath.lvl", 90),
    ("rm_nl_shrinepath2vault.lvl", 91),
    ("rm_nx_cave01.lvl", 92),
    ("rm_nx_shrinepath_2.lvl", 93),
    ("rm_nx_mooncourtyard.lvl", 94),
    ("rm_nx_towerlock.lvl", 95),
    ("rm_nc_cliffcampfire.lvl", 96),
    ("rm_nl_tobrokenshallows.lvl", 97),
    ("rm_nx_stairs03.lvl", 98),
    ("rm_nl_warproom.lvl", 100),
    ("rm_nl_crushwarphall.lvl", 101),
    ("rm_nl_crushtransition.lvl", 102),
    ("rm_nl_crushbackloop.lvl", 103),
    ("rm_nc_crusharena.lvl", 104),
    ("rm_nl_dropspiralopen.lvl", 106),
    ("rm_nl_droppits.lvl", 107),
    ("rm_nl_dropblockcultfight.lvl", 108),
    ("rm_nl_droparena.lvl", 109),
    ("rm_nl_gapopening.lvl", 111),
    ("rm_nx_gapwide.lvl", 112),
    ("rm_nl_gaphallway.lvl", 113),
    ("rm_nl_risingarena.lvl", 114),
    ("rm_nx_cathedralentrance.lvl", 116),
    ("rm_nx_cathedralhall.lvl", 117),
    ("rm_nl_altarthrone.lvl", 118),
    ("rm_nx_spiralstaircase.lvl", 119),
    ("rm_nx_librariantablet.lvl", 120),
    ("rm_nx_jerkpope.lvl", 121),
    ("rm_nl_stairascent.lvl", 123),
    ("rm_nl_crusharena.lvl", 124),
    ("rm_sx_southopening.lvl", 128),
    ("rm_ch_ctemplate.lvl", 129),
    ("rm_sx_towersouth.lvl", 130),
    ("rm_sx_npc.lvl", 131),
    ("rm_s_gauntlet_elevator.lvl", 132),
    ("rm_ch_bgunpillars.lvl", 133),
    ("rm_ch_bfinal.lvl", 134),
    ("rm_s_gauntletend.lvl", 135),
    ("rm_ch_bdirkdemolition.lvl", 137),
    ("rm_ch_tabigone.lvl", 139),
    ("rm_ch_cgateblock.lvl", 140),
    ("rm_ch_bmaddash.lvl", 141),
    ("rm_ch_tlongestroad.lvl", 142),
    ("rm_s_bulletbaker.lvl", 143),
    ("rm_ch_cendhall.lvl", 144),
    ("rm_ch_cturnhall.lvl", 146),
    ("rm_ch_bfps.lvl", 147),
    ("rm_ch_cbigggns.lvl", 148),
    ("rm_ch_cspawnground.lvl", 149),
    ("rm_s_countaculard.lvl", 150),
    ("rm_ch_acorner.lvl", 152),
    ("rm_ch_bdirkdeluge.lvl", 154),
    ("rm_ch_bpods.lvl", 155),
    ("rm_ch_bgundirkdash.lvl", 156),
    ("rm_s_markscythe.lvl", 157),
    ("rm_s_gauntletlinkup.lvl", 158),
    ("rm_ch_apillarbird.lvl", 160),
    ("rm_ch_cspiral.lvl", 161),
    ("rm_ch_tbirdstandoff.lvl", 162),
    ("rm_ch_bleaperfall.lvl", 163),
    ("rm_s_bennyarrow.lvl", 164),
    ("rm_s_gauntlettitanfinale.lvl", 165),
    ("rm_ea_eastopening.lvl", 171),
    ("rm_ec_swordbridge.lvl", 172),
    ("rm_el_flameelevatorenter.lvl", 173),
    ("rm_ea_watertunnellab.lvl", 174),
    ("rm_ec_theplaza.lvl", 175),
    ("rm_ec_npcdrugden.lvl", 176),
    ("rm_ex_towereast.lvl", 177),
    ("rm_eb_bogstreet.lvl", 178),
    ("rm_ec_plazatoloop.lvl", 179),
    ("rm_el_megahugelab.lvl", 181),
    ("rm_eb_meltymasharena.lvl", 182),
    ("rm_eb_flamepitlab.lvl", 183),
    ("rm_el_flameelevatorexit.lvl", 184),
    ("rm_eb_deadotterwalk.lvl", 185),
    ("rm_ec_plazaaccesslab.lvl", 187),
    ("rm_ec_dockslab.lvl", 188),
    ("rm_ex_dockscampfire.lvl", 189),
    ("rm_ev_docksbridge.lvl", 190),
    ("rm_el_frogarena.lvl", 191),
    ("rm_ec_bigboglab.lvl", 193),
    ("rm_ea_bogtemplecamp.lvl", 194),
    ("rm_ea_frogboss.lvl", 195),
    ("rm_ec_templeishvault.lvl", 196),
    ("rm_ec_eastloop.lvl", 198),
    ("rm_ec_looplab.lvl", 199),
    ("rm_eb_meltyleaperarena.lvl", 200),
    ("rm_ec_plazatodocks.lvl", 202),
    ("rm_ea_dockfightlab.lvl", 203),
    ("rm_eb_underotterbigriflerumble.lvl", 204),
    ("rm_eb_cleanershole.lvl", 205),
    ("rm_wa_entrance.lvl", 209),
    ("rm_wl_prisonhalvault.lvl", 210),
    ("rm_wa_deadwood.lvl", 211),
    ("rm_wa_deadwoods1.lvl", 212),
    ("rm_wa_grotto_buffintro.lvl", 213),
    ("rm_wc_windingwood.lvl", 214),
    ("rm_wc_grottonpc.lvl", 215),
    ("rm_wl_npctreehouse.lvl", 216),
    ("rm_wc_minilab.lvl", 217),
    ("rm_wt_thewood.lvl", 218),
    ("rm_wa_entswitch.lvl", 219),
    ("rm_wc_meadowoodcorner.lvl", 220),
    ("rm_wb_treetreachery.lvl", 222),
    ("rm_wl_westdriftervault.lvl", 223),
    ("rm_wt_slowlab.lvl", 225),
    ("rm_wc_cliffsidecellsredux.lvl", 226),
    ("rm_wc_prisonhal.lvl", 227),
    ("rm_wc_thinforest.lvl", 229),
    ("rm_wc_simplepath.lvl", 230),
    ("rm_wc_crystallake.lvl", 231),
    ("rm_wc_crystallakevault.lvl", 232),
    ("rm_wc_prisonhallend.lvl", 233),
    ("rm_wc_thinforestlow.lvl", 234),
    ("rm_wc_thinforestlowsecret.lvl", 235),
    ("rm_wa_titanfalls.lvl", 236),
    ("rm_wa_vale.lvl", 238),
    ("rm_wc_bigmeadow.lvl", 239),
    ("rm_wc_bigmeadowvault.lvl", 240),
    ("rm_wc_meadowcavecrossing.lvl", 241),
    ("rm_wb_bigbattle.lvl", 242),
    ("rm_wb_tanukitrouble.lvl", 243),
    ("rm_wc_ruinclearing.lvl", 244),
    ("rm_wx_boss.lvl", 245),
    ("rm_wa_towerenter.lvl", 246),
    ("rm_wa_multientrancelab.lvl", 247),
    ("rm_wa_crsytaldescent.lvl", 248),
    ("rm_wa_grottox.lvl", 250),
    ("rm_wb_crystalqueen.lvl", 251),
    ("rm_wt_protogrid.lvl", 252),
    ("rm_wv_puzzlepalacenew.lvl", 253),
    ("rm_a_elevatorshaftupper.lvl", 256),
    ("rm_a_elevatorshaft.lvl", 257),
    ("rm_a_predownward.lvl", 258),
    ("rm_a_downward.lvl", 259),
    ("rm_a_downwarddead.lvl", 260),
    ("rm_a_downwarddeadrevisit.lvl", 261),
    ("rm_a_emberroom.lvl", 262),
    ("rm_bossrush_hub.lvl", 265),
    ("rm_bossrush_frogboss.lvl", 266),
    ("rm_bossrush_jerkpope.lvl", 267),
    ("rm_bossrush_general.lvl", 268),
    ("rm_bossrush_bulletbaker.lvl", 269),
    ("rm_bossrush_countaculard.lvl", 270),
    ("rm_bossrush_markscythe.lvl", 271),
    ("rm_bossrush_bennyarrow.lvl", 272),
    ("rm_bossrush_ember.lvl", 273),
    ("rm_c_drifterworkshop.lvl", 276)
}


def get_id_from_name(name: str) -> int:
    """
    A way to convert level name to its internal ID.
    Not case sensitive.
    """
    for namee, idd in level_names_and_ids:
        if namee == name.lower():
            return idd
    raise HLDError(f"No such level named {name}.")


def get_name_from_id(id_: int) -> str:
    """
    A way to convert internal level ID to its name.
    Returns in lowercase.
    """
    for namee, idd in level_names_and_ids:
        if idd == id_:
            return namee
    raise HLDError(f"No such level with id {id_}.")
