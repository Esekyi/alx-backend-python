#!/usr/bin/env python3
"""
type-annotated function which takes list of
int and floats, and returns a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum_mixed_list: takes list of int and float
    params: mxd_lst: float | int
    Returns: float
    """
    total_sum: float = 0.0
    for item in mxd_lst:
        total_sum += item
    return total_sum
