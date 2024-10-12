#!/usr/bin/env python3
"""
function which takes in list of floats
and return the sum of floats
Returns: float
"""
from typing import List



def sum_list(input_list: List[float]) -> float:
    """
    sum_list: takes in list of float
    Params: input_list[]
    Returns: float
    """
    total: float = 0.0
    for item in input_list:
        total += item
    return total
