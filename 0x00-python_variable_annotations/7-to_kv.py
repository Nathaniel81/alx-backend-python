#!/usr/bin/env python3
"""
Contains a function to_kv that takes a string k and an int or float v
as arguments and returns a tuple where the first element is k and the
second element is the square of v."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string k as the first element and the square of an
    int or float v as the second element
    """
    return k, v ** 2
