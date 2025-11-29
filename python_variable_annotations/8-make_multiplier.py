#!/usr/bin/env python3
"""
    Create a multiplier function that multiplies its
    input by the given multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function that multiplies its
    input by the given multiplier.
    """
    def multiply(value: float) -> float:
        return value * multiplier

    return multiply
