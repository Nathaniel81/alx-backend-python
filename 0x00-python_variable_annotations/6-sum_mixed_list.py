#!/usr/bin/env python3
"""
Provides a type-annotated function which takes a list of integers and floats
and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of numbers in the list"""
    return sum(mxd_lst)
