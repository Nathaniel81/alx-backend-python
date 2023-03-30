#!/usr/bin/env python3
"""
Contains a type-annotated function that takes a float as argument
and returns a fuction that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by the given multiplier"""
    def multiplier_func(x: float) -> float:
        """Returns the result of multiplying it by the given multiplier"""
        return x * multiplier
    return multiplier_func
