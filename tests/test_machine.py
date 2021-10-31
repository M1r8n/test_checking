import pytest

from Machine.Machine import *

@pytest.mark.parametrize("test_input,expected", [
    ('12',12),
    ('13',13),
    ('01',1),
])
def test_conversion(test_input,expected):
    assert int(test_input) is expected

def test_Machine():
    m1=Machine()
    assert m1.checkState() is States.Free
    m1.reserveMachine()
    assert m1.checkState() is States.Busy
    m1.turnOff()
    assert m1.checkState() is States.Offline

@pytest.mark.xfail
def test_divide_by_zero():
    assert 1 / 0 == 1
