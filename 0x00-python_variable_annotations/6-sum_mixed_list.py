#!/usr/bin/env python3
from typing import List, Union
''' for checker
;;;
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    ''' [pls] [send]
    '''
    sum: float = 0
    for ele in mxd_lst:
        sum += ele
    return sum
