#!/usr/bin/env python3
"""Task 10 module.
"""
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    This function retrieves the first element of a sequence,
    safely handling empty list.
    """
    if lst:
        return lst[0]
    else:
        return None
