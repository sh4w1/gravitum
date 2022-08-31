"""Implement functions which are used in the code decompiled by Ghidra."""

from typing import Type, TypeVar

from .ida import _truncate, cfadd, ofsub, ofadd
from ..integer import IntVar, int8, int16, int32, int64, uint8, uint16, uint32, uint64
from ..utils import get_type

# Refer to https://github.com/NationalSecurityAgency/ghidra/blob/master/Ghidra/Features/Decompiler/src/main/help/help/topics/DecompilePlugin/DecompilerConcepts.html    # noqa: E501

_T = TypeVar("_T", int8, int16, int32, int64, uint8, uint16, uint32, uint64)


def _zero_extend(x: IntVar, to_type: Type[_T]) -> _T:
    """Zero-extension operator."""
    return to_type.from_bytes(x.to_bytes())


def _sign_extend(x: IntVar, to_type: Type[_T]) -> _T:
    """Sign-extension operator."""
    t1 = get_type(size=x.get_size(), signed=True)
    t2 = get_type(size=to_type.get_size(), signed=True)
    return to_type.from_bytes(t2.from_bytes(t1(x).to_bytes()).to_bytes())


def sub21(x: uint16, c: int) -> uint8:
    """Implementation of `SUB21`."""
    return _truncate(x, c, uint8)


def sub41(x: uint32, c: int) -> uint8:
    """Implementation of `SUB41`."""
    return _truncate(x, c, uint8)


def sub42(x: uint32, c: int) -> uint16:
    """Implementation of `SUB42`."""
    return _truncate(x, c, uint16)


def sub81(x: uint64, c: int) -> uint8:
    """Implementation of `SUB81`."""
    return _truncate(x, c, uint8)


def sub82(x: uint64, c: int) -> uint16:
    """Implementation of `SUB82`."""
    return _truncate(x, c, uint16)


def sub84(x: uint64, c: int) -> uint32:
    """Implementation of `SUB84`."""
    return _truncate(x, c, uint32)


def zext12(x: uint8) -> uint16:
    """Implementation of `ZEXT12`."""
    return _zero_extend(x, uint16)


def zext14(x: uint8) -> uint32:
    """Implementation of `ZEXT14`."""
    return _zero_extend(x, uint32)


def zext18(x: uint8) -> uint64:
    """Implementation of `ZEXT18`."""
    return _zero_extend(x, uint64)


def zext24(x: uint16) -> uint32:
    """Implementation of `ZEXT14`."""
    return _zero_extend(x, uint32)


def zext28(x: uint16) -> uint64:
    """Implementation of `ZEXT18`."""
    return _zero_extend(x, uint64)


def zext48(x: uint32) -> uint64:
    """Implementation of `ZEXT48`."""
    return _zero_extend(x, uint64)


def sext12(x: uint8) -> uint16:
    """Implementation of `SEXT12`."""
    return _sign_extend(x, uint16)


def sext14(x: uint8) -> uint32:
    """Implementation of `SEXT14`."""
    return _sign_extend(x, uint32)


def sext18(x: uint8) -> uint64:
    """Implementation of `SEXT18`."""
    return _sign_extend(x, uint64)


def sext24(x: uint16) -> uint32:
    """Implementation of `SEXT14`."""
    return _sign_extend(x, uint32)


def sext28(x: uint16) -> uint64:
    """Implementation of `SEXT18`."""
    return _sign_extend(x, uint64)


def sext48(x: uint32) -> uint64:
    """Implementation of `SEXT48`."""
    return _sign_extend(x, uint64)


def sborrow1(x: uint8, y: uint8) -> int:
    """Implementation of `SBORROW1`."""
    return ofsub(x, y)


def sborrow2(x: uint16, y: uint16) -> int:
    """Implementation of `SBORROW2`."""
    return ofsub(x, y)


def sborrow4(x: uint32, y: uint32) -> int:
    """Implementation of `SBORROW4`."""
    return ofsub(x, y)


def sborrow8(x: uint64, y: uint64) -> int:
    """Implementation of `SBORROW8`."""
    return ofsub(x, y)


def carry1(x: uint8, y: uint8) -> int:
    """Implementation of `CARRY1`."""
    return cfadd(x, y)


def carry2(x: uint16, y: uint16) -> int:
    """Implementation of `CARRY2`."""
    return cfadd(x, y)


def carry4(x: uint32, y: uint32) -> int:
    """Implementation of `CARRY4`."""
    return cfadd(x, y)


def carry8(x: uint64, y: uint64) -> int:
    """Implementation of `CARRY8`."""
    return cfadd(x, y)


def scarry1(x: int8, y: int8) -> int:
    """Implementation of `SCARRY1`."""
    return ofadd(x, y)


def scarry2(x: int16, y: int16) -> int:
    """Implementation of `SCARRY2`."""
    return ofadd(x, y)


def scarry4(x: int32, y: int32) -> int:
    """Implementation of `SCARRY4`."""
    return ofadd(x, y)


def scarry8(x: int64, y: int64) -> int:
    """Implementation of `SCARRY8`."""
    return ofadd(x, y)
