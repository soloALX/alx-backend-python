#!/usr/bin/env python3

'''
Use `mypy` to validate the following
piece of code and apply any necessary changes.
'''


import typing
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


if __name__ == '__main__':
    array = [12, 72, 91]

    zoom_2x = zoom_array(array)

    zoom_3x = zoom_array(array, 3.0)
