from _pytest.tmpdir import tmp_path
from hldlib import Counter, find_path, HLDError, default_load, HLDLevel
from pathlib import Path
from _fixtures import testing_level
import pytest
import sys


def test_counter():  # Why?
    a = Counter(1)
    assert a.use() == 2
    assert a.use() == 3
    assert a.use() == 4


def test_find_path(tmp_path: Path):
    with pytest.raises(HLDError):
        find_path("hlddir.txt", tmp_path)
    sub = tmp_path / "sub"
    sub.mkdir()
    hlddir = sub / "hlddir.txt"
    hlddir.write_text("C://...")
    assert find_path("hlddir.txt", tmp_path) == "C://..."


def test_default_load_win(tmp_path: Path, testing_level: HLDLevel):
    sys.platform = "win32"

    north = tmp_path / "North"
    north.mkdir()
    testing_level.dump(north)
    east = tmp_path / "East"
    east.mkdir()
    testing_level.dump(east)
    west = tmp_path / "West"
    west.mkdir()
    testing_level.dump(west)
    south = tmp_path / "South"
    south.mkdir()
    testing_level.dump(south)
    central = tmp_path / "Central"
    central.mkdir()
    testing_level.dump(central)
    intro = tmp_path / "Intro"
    intro.mkdir()
    testing_level.dump(intro)
    abyss = tmp_path / "Abyss"
    abyss.mkdir()
    testing_level.dump(abyss)
    loaded = default_load(tmp_path)
    assert len(loaded) == 7
    assert loaded[0].direction != loaded[1].direction

def test_default_load_linux(tmp_path: Path, testing_level: HLDLevel):
    sys.platform = "linux"

    assets = tmp_path / "assets"; assets.mkdir()
    north = assets / "north"; north.mkdir(); testing_level.dump(north)
    east = assets / "east"; east.mkdir(); testing_level.dump(east)
    west = assets / "west"; west.mkdir(); testing_level.dump(west)
    south = assets / "south"; south.mkdir(); testing_level.dump(south)
    central = assets / "central"; central.mkdir(); testing_level.dump(central)
    intro = assets / "intro"; intro.mkdir(); testing_level.dump(intro)
    abyss = assets / "abyss"; abyss.mkdir(); testing_level.dump(abyss)
    loaded = default_load(tmp_path) 
    assert len(loaded) == 7
    assert loaded[0].direction != loaded[1].direction

def test_default_load_macos(tmp_path: Path, testing_level: HLDLevel):
    sys.platform = "darwin"

    hldapp = tmp_path / "HyperLightDrifter.app"; hldapp.mkdir()
    contents = hldapp / "Contents"; contents.mkdir()
    res = contents / "Resources"; res.mkdir()
    north = res / "north"; north.mkdir(); testing_level.dump(north)
    east = res / "east"; east.mkdir(); testing_level.dump(east)
    west = res / "west"; west.mkdir(); testing_level.dump(west)
    south = res / "south"; south.mkdir(); testing_level.dump(south)
    central = res / "central"; central.mkdir(); testing_level.dump(central)
    intro = res / "intro"; intro.mkdir(); testing_level.dump(intro)
    abyss = res / "abyss"; abyss.mkdir(); testing_level.dump(abyss)
    loaded = default_load(tmp_path) 
    assert len(loaded) == 7
    assert loaded[0].direction != loaded[1].direction
