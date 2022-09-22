import re

from . import endian
from .integer import int8, int16, int32, int64, uint8, uint16, uint32, uint64


def get_type(size=None, signed=None, type_name=None):
    """Get type int with specified size and signed.

    Args:
        size: The size of the type.
        signed: Is the type signed.
        type_name: The lowercase name of type to find. If it is None,
            ``size`` and ``signed`` must be given.

    Raises:
        ValueError: If no matched type.
    """
    int_types = [int8, int16, int32, int64, uint8, uint16, uint32, uint64]

    if type_name is not None:
        match = re.match(r"(u*)int(\d+)", type_name)

        if match:
            nbits = int(match.group(2))
            if nbits % 8 == 0:
                signed = not bool(match.group(1))
                size = nbits // 8

    if size is not None and signed is not None:
        for int_type in int_types:
            if int_type.get_size() == size and int_type.get_signed() == signed:
                return int_type

    raise ValueError("No matched type")


def set_endian(little=True):
    """Set global endian."""
    endian.BYTE_ORDER = endian.LITTLE_ENDIAN if little else endian.BIG_ENDIAN
