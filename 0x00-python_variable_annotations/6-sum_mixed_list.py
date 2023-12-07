#!/usr/bin/env python3
"""Task 6 module.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function takes a list of integers and floats
    as an argument and returns their sum as a float
    """
    total = 0.0
    for num in mxd_lst:
        # Convert integers to floats
        num = float(num)
        total += num

    return total
