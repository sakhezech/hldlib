import pytest
from _fixtures import testing_obj_string

from hldlib import CaseScriptType, Dependencies, HLDError, HLDObj, HLDType


def test_from_string(testing_obj_string: str):
    obj = HLDObj.from_string(testing_obj_string)
    assert obj.type == HLDType.SPAWNER
    assert obj.uid == 593
    assert obj.x == 536
    assert obj.y == 352
    assert obj.layer == 6
    assert obj.dependencies == Dependencies(
        [], CaseScriptType.NO, False, '-999999', 0
    )
    assert obj.attrs == {
        '-1': 'dirk',
        '-2': -999999,
        '-4': 1,
        '-5': 0,
        '-6': -1,
        '-7': 0,
        '-8': 0,
    }
    obj2 = HLDObj.from_string(
        'obj,Spawner,5493,296,920,3,1,4759,++,-1=Gearbit,-2=-999999,-4=1,-5=0,-6=-1,-7=0,-8=0,'
    )
    assert obj2.dependencies == Dependencies(
        [4759], CaseScriptType.NO, False, '-999999', 0
    )
    obj3 = HLDObj.from_string(
        'obj,Region,6132,584,784,3,-999999,caseScript,2,1,char,0,++,0=16,1=48,'
    )
    assert obj3.dependencies == Dependencies(
        [], CaseScriptType.REGION, False, HLDType.CHAR, 0
    )
    obj4 = HLDObj.from_string(
        'obj,EmptyObject,4599,560,400,6,2,593,4113,caseScript,4,0,-999999,5,++,mn=Dirk DEAD,a=-1,'
    )
    assert obj4.dependencies == Dependencies(
        [593, 4113], CaseScriptType.ENEMY, True, '-999999', 5
    )


def test_from_string_errors():
    with pytest.raises(HLDError):
        HLDObj.from_string('')
    with pytest.raises(HLDError):
        HLDObj.from_string(
            ',obj,Spawner,593,536,352,6,-999999,++,-1=dirk,-2=-999999,-4=1,-5=0,-6=-1,-7=0,-8=0,'
        )
    with pytest.raises(HLDError):
        HLDObj.from_string(
            'obj,Spawner,593,536,6,-999999,++,-1=dirk,-2=-999999,-4=1,-5=0,-6=-1,-7=0,-8=0,'
        )


def test_to_string(testing_obj_string: str):
    obj = HLDObj.from_string(testing_obj_string)
    assert testing_obj_string == obj.to_string().strip().replace('//', '')
