#!/usr/bin/env python3
"""
An iterable containing sequences.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples,
    each containing a sequence from the iterable and its length.
    Args:
        lst (Iterable[Sequence]): An iterable containing sequences.
    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each with a sequence
        and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
