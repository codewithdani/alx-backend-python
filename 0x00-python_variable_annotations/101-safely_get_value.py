#!/usr/bin/env python3
"""Task 11 module.
"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """Safely retrieves a value from a dictionary,
    returning a default value if the key is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
