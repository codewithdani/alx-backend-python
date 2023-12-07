#!/usr/bin/env python3
"""Task 7 module.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function takes a string key and an integer or float
    value as arguments and returns a tuple containing the key
    and the square of the value.
    """
    return (k, float(v**2))
