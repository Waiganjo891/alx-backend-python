#!/usr/bin/env python3
"""
This module provides a function to create a multiplier function.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function.
    
    Args:
        multiplier (float): The multiplier value.
    
    Returns:
        Callable[[float], float]: A function that multiplies a float by the given multiplier.
    """
    
    def multiplier_func(x: float) -> float:
        """
        Multiplies a float by the outer multiplier.
        
        Args:
            x (float): The value to be multiplied.
        
        Returns:
            float: The result of the multiplication.
        """
        return x * multiplier
    
    return multiplier_func
