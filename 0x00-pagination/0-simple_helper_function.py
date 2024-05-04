#!/usr/bin/env python3
"""0-simple_helper_function.py"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    '''Returns tuple of integers
        Args:
            page (int): page number.
            page_size (int): number of data in a page.
    '''
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
