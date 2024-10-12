#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function of float typed
    """
    def multiplier_func(x: float) -> float:
        """
        computes the actual multiplier
        Returns a float
        """
        return x * multiplier
    return multiplier_func
