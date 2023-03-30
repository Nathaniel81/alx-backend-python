#!/usr/bin/env python3
"""
Contains a function that returns a list of tuples where each tuple contains
an element from the input iterable and its length
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    A list of tuples where each tuple contains an
    element from the input iterable and its length
    """
    return [(i, len(i)) for i in lst]
