#!/usr/bin/env python3
"""
Convert a key and a value into a tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Convert a key and a value into a tuple."""
    return (k, float(v**2))
