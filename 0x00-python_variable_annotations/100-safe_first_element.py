#!/usr/bin/env python3
"""Duck typing - first element of a sequence
"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    duck-typed.
    safe_first_element - returns first element of lst or
    None if lst isn't a Sequence (list, tuples, strings)
    """
    return lst[0] if lst else None
