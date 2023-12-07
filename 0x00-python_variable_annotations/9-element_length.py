#!/usr/bin/env python3
"""Task 9's module.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function takes a list of any type and returns
    a list of tuples containing the element and its length.
    """
    return [(i, len(i)) for i in lst]
