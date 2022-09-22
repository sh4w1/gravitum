from ..integer import int8, int16, int32, int64, uint8, uint16, uint32, uint64

def sub21(x: uint16, c: int) -> uint8: ...
def sub41(x: uint32, c: int) -> uint8: ...
def sub42(x: uint32, c: int) -> uint16: ...
def sub81(x: uint64, c: int) -> uint8: ...
def sub82(x: uint64, c: int) -> uint16: ...
def sub84(x: uint64, c: int) -> uint32: ...
def zext12(x: uint8) -> uint16: ...
def zext14(x: uint8) -> uint32: ...
def zext18(x: uint8) -> uint64: ...
def zext24(x: uint16) -> uint32: ...
def zext28(x: uint16) -> uint64: ...
def zext48(x: uint32) -> uint64: ...
def sext12(x: uint8) -> uint16: ...
def sext14(x: uint8) -> uint32: ...
def sext18(x: uint8) -> uint64: ...
def sext24(x: uint16) -> uint32: ...
def sext28(x: uint16) -> uint64: ...
def sext48(x: uint32) -> uint64: ...
def sborrow1(x: uint8, y: uint8): ...
def sborrow2(x: uint16, y: uint16): ...
def sborrow4(x: uint32, y: uint32): ...
def sborrow8(x: uint64, y: uint64): ...
def carry1(x: uint8, y: uint8): ...
def carry2(x: uint16, y: uint16): ...
def carry4(x: uint32, y: uint32): ...
def carry8(x: uint64, y: uint64): ...
def scarry1(x: int8, y: int8): ...
def scarry2(x: int16, y: int16): ...
def scarry4(x: int32, y: int32): ...
def scarry8(x: int64, y: int64): ...