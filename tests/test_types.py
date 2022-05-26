import pytest

from gravitum import int8, uint8, uint32, UInt8, UInt32
from gravitum.utils import disable_numpy_overflow_warnings

disable_numpy_overflow_warnings()


@pytest.mark.parametrize('x,y,expected', [
    (int8(1), uint8(1), UInt8),
    (uint8(1), 1, UInt8),
    (uint8(1), uint32(1), UInt32),
])
def test_type_conversion(x, y, expected):
    result = x + y

    assert type(result) == expected


@pytest.mark.parametrize('x,y,expected', [
    (uint32(0x53683477), uint32(0x53683477), 0xd5708f51),
])
def test_overflow(x, y, expected):
    result = x * y

    assert result == expected
