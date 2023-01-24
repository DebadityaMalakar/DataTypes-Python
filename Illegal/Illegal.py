
import ctypes
import sys

def mutate(obj, new_obj):
    """
    Use only if you are expert in python and know what you are doing.
    """
    if sys.getsizeof(obj) != sys.getsizeof(new_obj):
        raise ValueError('objects must have same size')

    mem = (ctypes.c_byte * sys.getsizeof(obj)).from_address(id(obj))
    new_mem = (ctypes.c_byte * sys.getsizeof(new_obj)).from_address(id(new_obj))

    for i in range(len(mem)):
        mem[i] = new_mem[i]
