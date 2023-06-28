from pathlib import Path
from hldlib import HLDDirection, HLDLevel, HLDObj, get_id_from_name, get_name_from_id, HLDError
from os.path import join as p_join
from _fixtures import testing_level
import copy
import pytest


def test_dump_and_load(tmp_path: Path, testing_level: HLDLevel):
    testing_level.dump(tmp_path)
    dumped_level = HLDLevel.load(
        p_join(tmp_path, testing_level.name), HLDDirection.ABYSS)
    assert testing_level == dumped_level


def test_load_errors(tmp_path: Path, testing_level: HLDLevel):

    level1 = copy.deepcopy(testing_level)
    level1.layer_names = {}
    level1.name = "rm_A_Test1.lvl"
    level1.dump(tmp_path)

    level2 = copy.deepcopy(testing_level)
    level2.date = ''  # type: ignore
    level2.name = "rm_A_Test2.lvl"
    level2.dump(tmp_path)

    level3 = copy.deepcopy(testing_level)
    level3.room_settings = {}
    level3.name = "rm_A_Test3.lvl"

    with pytest.raises(IndexError):
        HLDLevel.load(p_join(tmp_path, level1.name), HLDDirection.ABYSS)

    with pytest.raises(ValueError):
        HLDLevel.load(p_join(tmp_path, level2.name), HLDDirection.ABYSS)

    with pytest.raises(KeyError):
        level3.dump(tmp_path)


def test_get_ids_and_names():
    assert get_id_from_name("rm_in_01_brokenshallows.lvl") == 46
    assert get_name_from_id(46) == "rm_in_01_brokenshallows.lvl"


def test_ids_and_names_errors():
    with pytest.raises(HLDError):
        get_id_from_name("rm_A_DoesntExist.lvl")
    with pytest.raises(HLDError):
        get_name_from_id(0)
