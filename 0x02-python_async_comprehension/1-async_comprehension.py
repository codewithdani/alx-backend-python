#!/usr/bin/env python3
"""
Task 1 module.
"""
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    This coroutine asynchronously generates
    10 random numbers between 0 and 10.
    """
    return [num async for num in async_generator()]
