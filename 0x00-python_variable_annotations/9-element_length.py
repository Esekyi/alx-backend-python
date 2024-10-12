#!/usr/bin/env python3
"""
Let's duck type an iterable object
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    function that takes an iterable of a given sequence
    Returns: List of tuples containing sequences and length
    of that element | int
    """

    return [(i, len(i)) for i in lst]
