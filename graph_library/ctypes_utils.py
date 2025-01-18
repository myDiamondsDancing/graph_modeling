import ctypes
from pathlib import Path

import numpy as np

clib: ctypes.CDLL = ctypes.CDLL(Path(__file__).parent / 'clib/build/lib.so')

# TODO: solve problem with pointers (why 2d used as 1d)
# define argtypes and restypes for functions
clib.has_route.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.uintp),
    ctypes.c_int32,
    ctypes.c_int32,
    ctypes.c_int32
]
clib.has_route.restype = ctypes.c_int8


def has_route(edges: np.ndarray, n: int, start: int, end: int) -> bool:
    return clib.has_route(
        edges.astype(np.uintp),
        ctypes.c_int32(n),
        ctypes.c_int32(start),
        ctypes.c_int32(end)
    ) == 1
