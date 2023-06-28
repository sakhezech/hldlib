from pathlib import Path
from hldlib import HLDSaveFile, hldsavefile
from os.path import join as p_join
from _fixtures import testing_savefile
import pytest


def test_load(testing_savefile: HLDSaveFile):
    assert testing_savefile.badass == 0.
    assert testing_savefile.mapMod == {"132": ["2"], "144": ["2"], "161": ["2"], "181": ["2"], "106": ["2"], "109": ["2"], "194": [
        "2"], "226": ["2"], "183": ["2"], "174": ["2"], "160": ["2"], "218": ["2"], "95": ["2"], "104": ["2"], "220": ["2"], "210": ["2"]}
    assert testing_savefile.dateTime == 44980.524126
    assert testing_savefile.healthUp == 0.
    assert testing_savefile.cl == {"9": ["101387", "185267", "206139", "266784"], "13": ["-1518851"], "7": ["-255100", "-187905",
                                                                                                            "-167326", "-53392"], "6": ["-1895481", "-1047430", "-932471", "-902212"], "8": ["-555279", "-398635", "-386457", "-676357"]}
    assert testing_savefile.destruct == {"-362246": ["163", "37.21"], "182612": ["218", "30.84"], "-1977913": ["220", "24.64"], "195297": ["219", "30.43"], "-368999": ["163", "37.21"], "204505": ["220", "24.64"], "204058": ["220", "24.64"], "205907": ["220", "24.64"], "203071": ["220", "24.64"], "-1821890": ["178", "15.82"], "-64910": ["193", "16.10"], "-1979001": ["209", "31.84"], "-1828684": ["171", "19.29"], "181376": ["218", "30.84"], "-215541": ["178", "15.82"], "-215122": ["178", "15.82"], "-214691": ["178", "15.82"], "-216282": ["178", "15.82"], "-1836176": ["163", "37.21"], "-1828020": ["171", "19.29"], "201096": ["220", "24.64"], "-1779408": ["220", "24.64"], "-48610": ["195", "17.29"], "-1780241": ["219", "30.43"], "207435": ["220", "24.64"], "-1915845": ["84", "2.77"], "-357070": ["164", "38.55"], "-213665": ["178", "15.82"], "-253672": ["174", "18.56"], "182104": ["218", "30.84"], "91576": ["209", "31.84"], "-212141": ["178", "15.82"], "-354348": ["164", "38.55"], "147348": ["214", "31.28"], "-217133": ["178", "15.82"], "94506": ["209", "31.84"], "-212024": ["178", "15.82"], "-252206": ["174", "18.56"], "-373395": ["162", "36.98"], "185525": ["218", "30.84"], "-1953605": ["46", "8.35"], "-271951": [
        "172", "19.04"], "-255797": ["174", "18.56"], "-212803": ["178", "15.82"], "183240": ["218", "30.84"], "-1821607": ["178", "15.82"], "185393": ["218", "30.84"], "-356716": ["164", "38.55"], "-287232": ["171", "19.29"], "146970": ["214", "31.28"], "-1779827": ["220", "24.64"], "204636": ["220", "24.64"], "194840": ["219", "30.43"], "-353066": ["164", "38.55"], "182418": ["218", "30.84"], "205862": ["220", "24.64"], "-42387": ["195", "17.29"], "-1774263": ["225", "30.15"], "-217053": ["178", "15.82"], "204535": ["220", "24.64"], "-353282": ["164", "38.55"], "-1781699": ["218", "30.84"], "187537": ["218", "30.84"], "-1805138": ["194", "17.47"], "207743": ["220", "24.64"], "-62416": ["193", "16.10"], "-213402": ["178", "15.82"], "-363367": ["163", "37.21"], "-218084": ["178", "15.82"], "-375514": ["162", "36.98"], "-67471": ["193", "16.10"], "-1532976": ["46", "8.35"], "203908": ["220", "24.64"], "-215793": ["178", "15.82"], "-212053": ["178", "15.82"], "203763": ["220", "24.64"], "-362348": ["163", "37.21"], "201428": ["220", "24.64"], "184155": ["218", "30.84"], "183939": ["218", "30.84"], "145253": ["214", "31.28"], "145792": ["214", "31.28"], "-48552": ["195", "17.29"], "-274723": ["172", "19.04"]}
    assert testing_savefile.values == {'ValuebadassOfficeState': ['2']}
    assert testing_savefile.gunReminderTimes == 0.
    assert testing_savefile.fireplaceSave == 0.
    assert testing_savefile.checkHP == 5.
    assert testing_savefile.compShell == 0.
    assert testing_savefile.cSwords == ["0"]
    assert testing_savefile.cape == 0.
    assert testing_savefile.halluc == 0.
    assert testing_savefile.newcomerHoardeMessageShown == 0.
    assert testing_savefile.tutHeal == 0.
    assert testing_savefile.noSpawn == ['-1097954', '-145504', '-1871165']
    assert testing_savefile.checkY == 608.
    assert testing_savefile.specialUp == 0.
    assert testing_savefile.checkBat == 100.
    assert testing_savefile.noviceMode == 0.
    assert testing_savefile.successfulHealTimes == 5.
    assert testing_savefile.cCapes == ["0"]
    assert testing_savefile.CH == 0.
    assert testing_savefile.gear == 0.
    assert testing_savefile.checkCID == 624531.
    assert testing_savefile.rooms == ["46", "79", "47", "48", "49", "50", "53", "61", "62", "84", "85", "88", "90", "92", "93", "94", "104", "95", "106", "107", "108", "109", "96", "97", "64", "171", "172", "173", "174", "175", "177", "181", "182", "183", "184",
                                      "185", "178", "193", "194", "195", "196", "65", "209", "210", "211", "214", "218", "219", "220", "225", "226", "238", "248", "247", "246", "63", "128", "130", "144", "152", "160", "161", "162", "163", "164", "165", "132", "256", "257", "258", "259", "262"]
    assert testing_savefile.permaS == {"-1047940": ["2"], "-692232": [
        "2"], "-1387056": ["2"], "-697361": ["2"], "-183353": ["2"], "383989": ["2"]}
    assert testing_savefile.checkRoom == 262.
    assert testing_savefile.wellMap == ["1", "0", "2", "3"]
    assert testing_savefile.cShells == ["0"]
    assert testing_savefile.eq01 == 0.
    assert testing_savefile.tablet == []
    assert testing_savefile.successfulWarpTimes == 0.
    assert testing_savefile.skill == []
    assert testing_savefile.bosses == {'3.20': ['311', '226']}
    assert testing_savefile.scK == {'1': ['11']}
    assert testing_savefile.warp == ['0', '2', '3']
    assert testing_savefile.hasMap == 0.
    assert testing_savefile.events == ["-1534214", "-1517669", "-1497664", "-252694", "-226975", "-180659",
                                       "-174854", "-1824533", "-45677", "253426", "385501", "-396272", "-344922", "586666", "626776"]
    assert testing_savefile.gearReminderTimes == 0.
    assert testing_savefile.enemies == {"-186839": ["181", "12.14"], "-186271": ["181", "12.14"], "255598": ["225", "30.15", "spr_SmallCrystalSpiderDead", "1", "516", "698", "-1"], "251618": ["225", "30.15", "spr_RifleDirkDead", "1", "495", "720", "-1"], "-212825": ["178", "15.82", "spr_NinjaFrogDead", "1", "733", "162", "-1"], "-163409": ["183", "14.45"], "202959": ["220", "24.64", "spr_WolfDead", "1", "671", "373", "1"], "-914801": ["108", "7.63", "spr_CultBirdDead", "1", "582", "239", "-1"], "-1951270": ["48", "9.10", "spr_RifleDirkDead", "1", "1187", "1090", "1"], "255832": ["225", "30.15", "spr_SmallCrystalSpiderDead", "1", "597", "686", "1"], "-1937406": ["62", "2.37", "spr_DirkDead", "1", "522", "378", "-1"], "-166718": ["183", "14.45", "spr_RifleDirkDead", "1", "672", "917", "-1"], "471052": ["247", "29.58"], "-185752": ["181", "12.14"], "-63779": ["193", "16.10", "spr_RifleDirkDead", "1", "1097", "1473", "-1"], "-1346297": ["65", "32.08", "spr_SpiderDead", "1", "96", "434", "1"], "202483": ["220", "24.64", "spr_WolfDead", "1", "303", "244", "1"], "204267": ["220", "24.64", "spr_WolfDead", "1", "510", "352", "-1"], "-1523300": ["47", "8.71", "spr_DirkDead", "1", "781", "540", "-1"], "477748": ["247", "29.58"], "255772": ["225", "30.15", "spr_SmallCrystalSpiderDead", "1", "596", "690", "-1"], "-168686": ["183", "14.45"], "-397447": ["160", "36.16", "spr_MissileDirkDead", "1", "272", "893", "-1"], "-938573": ["106", "7.06", "spr_RifleDirkDead", "1", "369", "417", "1"], "256897": ["225", "30.15", "spr_SmallCrystalSpiderDead", "1", "814", "683", "1"], "-1518381": ["48", "9.10", "spr_DirkDead", "1", "1202", "1113", "-1"], "205619": ["220", "24.64", "spr_WolfDead", "1", "619", "333", "1"], "201283": ["220", "24.64", "spr_WolfDead", "1", "654", "376", "1"], "-387738": ["161", "36.54", "spr_RifleDirkDead", "1", "408", "146", "-1"], "-1816522": [
        "183", "14.45"], "185635": ["218", "30.84", "spr_TanukiDead", "1", "1196", "1062", "-1"], "204080": ["220", "24.64", "spr_WolfDead", "1", "562", "342", "1"], "-1816713": ["183", "14.45"], "-1375886": ["62", "2.37", "spr_DirkDead", "1", "504", "405", "-1"], "-164752": ["183", "14.45", "spr_RifleDirkDead", "1", "456", "779", "1"], "-1816137": ["183", "14.45", "spr_RifleDirkDead", "1", "641", "1088", "-1"], "-62566": ["193", "16.10", "spr_DirkDead", "1", "1287", "1454", "-1"], "202315": ["220", "24.64", "spr_WolfDead", "1", "507", "371", "-1"], "142529": ["214", "31.28", "spr_DirkDead", "1", "1228", "993", "-1"], "-1821511": ["178", "15.82", "spr_NinjaFrogDead", "1", "691", "199", "1"], "-1774601": ["225", "30.15", "spr_SmallCrystalSpiderDead", "1", "761", "660", "1"], "-168534": ["183", "14.45"], "-1356259": ["64", "19.63", "spr_SpiderDead", "1", "421", "225", "1"], "-217560": ["178", "15.82", "spr_JarFrogDead", "1", "887", "319", "1"], "-167717": ["183", "14.45", "spr_RifleDirkDecapBottom", "1", "456", "761", "-1"], "-934904": ["106", "7.06", "spr_RifleDirkDead", "1", "356", "449", "1"], "255460": ["225", "30.15", "spr_RifleDirkDead", "1", "623", "676", "1"], "-63679": ["193", "16.10", "spr_DirkDead", "1", "1346", "1446", "-1"], "-1836741": ["163", "37.21"], "203862": ["220", "24.64", "spr_WolfDead", "1", "652", "358", "-1"], "203066": ["220", "24.64", "spr_WolfDead", "1", "507", "340", "1"], "-212353": ["178", "15.82", "spr_JarFrogDead", "1", "921", "201", "-1"], "-1353398": ["64", "19.63", "spr_SpiderDead", "1", "403", "214", "1"], "251259": ["225", "30.15", "spr_SmallCrystalSpiderDead", "1", "832", "694", "1"], "-165301": ["183", "14.45", "spr_DirkDead", "1", "648", "897", "-1"], "-165346": ["183", "14.45", "spr_RifleDirkDead", "1", "673", "1088", "1"], "-1514532": ["48", "9.10", "spr_DirkDead", "1", "1245", "1094", "-1"], "-164347": ["183", "14.45"]}
    assert testing_savefile.scUp == []
    assert testing_savefile.checkX == 347.
    assert testing_savefile.bossGearbits == []
    assert testing_savefile.cues == ["-1092019", "-1092517", "-1073366",
                                     "-1055576", "-276126", "-1814127", "-147547", "-214027", "-716092"]
    assert testing_savefile.playT == 41.
    assert testing_savefile.well == ['1', '0', '2', '3']
    assert testing_savefile.sc == ["1"]
    assert testing_savefile.drifterkey == 0.
    assert testing_savefile.successfulCollectTimes == 0.
    assert testing_savefile.checkAmmo == 0.
    assert testing_savefile.checkStash == 1.
    assert testing_savefile.charDeaths == 12.
    assert testing_savefile.eq00 == 1.
    assert testing_savefile.healthKits == ["-1533639", "-1527212", "-1527041", "-934951", "-1353463", "-166798",
                                           "-178664", "-63791", "-53836", "146225", "-1774222", "-387903", "-367621", "-342346", "-673207"]
    assert testing_savefile.sword == 0.
    assert testing_savefile.gameName == "Q"


def test_dump_and_load(tmp_path: Path, testing_savefile: HLDSaveFile):
    testing_savefile.dump(p_join(tmp_path, "hello.sav"))
    dumped_savefile = HLDSaveFile.load(p_join(tmp_path, "hello.sav"))
    assert testing_savefile == dumped_savefile


def test_dump_and_load_error(tmp_path: Path, testing_savefile: HLDSaveFile):
    with pytest.raises(Exception):
        testing_savefile.badass = ['1', '0', '2', '3']  # type: ignore
        testing_savefile.dump(p_join(tmp_path, "hello.sav"))
        HLDSaveFile.load(p_join(tmp_path, "hello.sav"))


def test_sflist():
    testing_sflist = hldsavefile.sflist.from_string("1+2+3+4+")
    testing_sflist.append("5")
    assert testing_sflist.to_string() == "1+2+3+4+5+"

    testing_sflist = hldsavefile.sflist.from_string("1+2+3+4+")
    testing_sflist.remove("2")
    assert testing_sflist.to_string() == "1+3+4+"

    testing_sflist = hldsavefile.sflist.from_string("")
    assert testing_sflist.to_string() == ""

    testing_sflist = hldsavefile.sflist.from_string("1+")
    assert testing_sflist.to_string() == "1+"


def test_sfdict():
    testing_sflist = hldsavefile.sfdict.from_string("1=1&2&3&>2=4&5&6&>")
    assert testing_sflist["1"] == ["1", "2", "3"]

    testing_sflist["3"] = ["7", "8", "9"]
    assert testing_sflist.to_string() == "1=1&2&3&>2=4&5&6&>3=7&8&9&>"

    testing_sflist = hldsavefile.sfdict()
    assert testing_sflist.to_string() == ""

    testing_sflist = hldsavefile.sfdict({"1": ["1"]})
    assert testing_sflist.to_string() == "1=1&>"
