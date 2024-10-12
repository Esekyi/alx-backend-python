#!/usr/bin/env python3
"""
Complex types - string and int/float to tuple
a function which takes a str k ot float v
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    to_kv: function that returns a tuple
    Params: k: str, v: int | float
    Returns: Tuple[k, v**2]
    """
    second_arg: float = v**2
    final_compute: Tuple[str, float] = (k, second_arg)

    return final_compute
