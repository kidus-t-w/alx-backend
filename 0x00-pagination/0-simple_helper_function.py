#!/usr/bin/env python3
"""0-simple_helper_function.py"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the range of indices for pagination.

    Args:
        page (int): The current page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index
        (inclusive) and end index (exclusive) of the range.
    """

    start_index: int = (page - 1) * page_size
    end_index: int = page * page_size
    return (start_index, end_index)
