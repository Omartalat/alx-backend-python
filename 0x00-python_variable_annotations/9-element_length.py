#!/usr/bin/env python3
"""
task 09
"""
from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    task 09
    """
    return [(i, len(i)) for i in lst]
