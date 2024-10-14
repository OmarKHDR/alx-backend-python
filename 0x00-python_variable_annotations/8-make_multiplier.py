#!/usr/bin/env python3
''' hello my nested function A file to function'''
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    '''
    Args:
        multiplier: of floats
    Return:
        function: Callable eee
    '''
    def mult(mul: float) -> float:
        return multiplier*mul
    return mult
