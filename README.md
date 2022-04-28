# Gravitum

Gravitum is a library for implementing decompiled code with Python.

## Requirements

- Python 3.6+

## Installation

```
$ pip install gravitum
```

## Usage

Gravitum defines some types (`Int8`, `Int16`, `Int32`, `Int64`, `UInt8`, `UInt16`, `UInt32`, `UInt64`) which based on the integer types of [numpy](https://github.com/numpy/numpy). You can use short-hand functions (`int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`) to create them.

```python
from gravitum import uint8

v = uint8(1)
```

Function `vptr` is provided to wrap `bytearray`, then you can operate it like a pointer.

For a C code:

```c
unsigned __int8 data[12] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};

unsigned __int8 *p = data;
unsigned __int8 v = p[3];

*((unsigned __int32 *)(p + 4) + 1) = v;
```

Write with Gravitum:

```python
from gravitum import vptr

data = bytearray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

p = vptr(data, 'uint8')
v = p.add(3).read()

p.add(4).cast('uint32').add(1).write(v)
```

Gravitum also implemented some functions (`ror*`, `rol*`, `bswap*`, `byte*`, `word*`, `dword*`, `clz`, etc.) which are used in the code decompiled by IDA. You can import them from `gravitum.hexrays`.

```python
from gravitum import uint32
from gravitum.hexrays import ror4

v = uint32(1)
v = ror4(v, 8)
```

