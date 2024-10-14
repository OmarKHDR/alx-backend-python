#!/usr/bin/env python3
''' function is just a function dont do interpreter work'''
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Args:
        lst: an interable of a sequence
    Return:
        A list of tuples of somethings
    '''
    return [(i, len(i)) for i in lst]
