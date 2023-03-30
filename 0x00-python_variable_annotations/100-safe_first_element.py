#!/usr/bin/env python3
"""Provides a function for safely getting the first element of an iterable"""
from typing import Sequence, Iterable, Union, Any


def safe_first_element(lst: Iterable(Sequence)) -> Union[Any, None]:
    """
    Returns the first element of an iterable if it exists,
    otherwise returns None.
    """
    if lst:
        return lst[0]
    else:
        return None
