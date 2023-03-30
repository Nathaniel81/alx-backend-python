#!/usr/bin/env python3
"""
Returns the value associated with a given key in a dictionary,
or a default value if the key is not present in the dictionary
"""
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')



def safely_get_value(dct: Mapping, key: Any, 
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Returns the value associated with the key in the dictionary,
    or the default value if the key is not present in the dictionary.
    If a default value is provided,
    the returned value will have the same type as the default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
