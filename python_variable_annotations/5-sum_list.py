#!/usr/bin/env python3
"""
    Function that gets a list of floats and return its sum
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function

    Args:
        input_list (list[float]): list of floats

    Return:
        float: sum of items
    """
    return sum(input_list)
