#!/usr/bin/env python3
"""
This module provides a function to sum a list of integers and floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of integers and floats and returns the result as a float.
    :param mxd_lst: A list containing integers and floats.
    :return: The sum of the list elements as a float.
    """
    return float(sum(mxd_lst))
