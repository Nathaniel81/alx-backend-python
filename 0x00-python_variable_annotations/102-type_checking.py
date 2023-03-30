#!/usr/bin/env python3
"""
Provides a function, zoom_array, which takes in a sequence and a zoom factor
and returns a new sequence that is zoomed in by the given factor
"""
from typing import List, Sequence, Tuple, Union


def zoom_array(lst: Sequence, factor: Union[int, float] = 2) -> List:
    """Returns a new list containing the zoomed in values"""
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3.0)
