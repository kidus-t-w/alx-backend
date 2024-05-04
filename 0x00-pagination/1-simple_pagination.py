#!/usr/bin/env python3
"""Calculate the range of indices for pagination."""

import csv
import math
from typing import Tuple, List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0, \
            "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be a positive integer"
        index = self.index_range(page, page_size)
        return self.dataset()[index[0]:index[1]]
