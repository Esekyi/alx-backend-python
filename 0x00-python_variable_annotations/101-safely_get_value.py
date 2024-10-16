#!/usr/bin/env python3
"""More involved type annotations"""
from typing import TypeVar, Mapping, Any, Union


T = TypeVar("T")


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    safely_get_value: Generics types usninf Typevar
    """

    return dct[key] if key in dct else default
