#!/usr/bin/env python3
"""
tash 10
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """task 10"""
    if lst:
        return lst[0]
    else:
        return None
