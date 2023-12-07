#!/usr/bin/env python3
"""Task 5 module.
"""


def sum_list(input_list: List[float]) -> float:
    """
    This function takes a list of floats as an argument
    and returns their sum as a floats
    """

    total = 0.0
    for element in input_list:
        total += element

    return total
