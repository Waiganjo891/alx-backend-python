#!/usr/bin/env python3
"""
This module provides utility functions for accessing nested maps.
"""


def access_nested_map(nested_map, path):
    """
    Access a nested object in `nested_map` with the sequence of keys in `path`.
    Args:
        nested_map (dict): A dictionary to access.
        path (tuple): A sequence of keys to access in the dictionary.
    Returns:
        The value found by traversing the nested_map with the given path.
    Raises:
        KeyError: If a key in the path is not found in the nested_map.
    """
    for key in path:
        nested_map = nested_map[key]
    return nested_map
