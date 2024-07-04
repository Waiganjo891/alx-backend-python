#!/usr/bin/env python3
"""
This module provides a function to create
a tuple with a string and the square of a number.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and an int or float and returns a tuple.
    The first element of the tuple is the string k.
    The second element is the square of the int/float v as a float.
    :param k: A string.
    :param v: An int or float.
    :return: A tuple where the first element is k
    and the second element is the square of v as a float.
    """
    return (k, float(v ** 2))
