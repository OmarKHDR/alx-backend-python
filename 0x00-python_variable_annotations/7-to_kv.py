#!/usr/bin/env python3
'''A file to function something that can be functioned'''
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    return (k, v*v)
