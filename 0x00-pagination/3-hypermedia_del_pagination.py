#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary containing the index, data, page_size, and next_index for a given index and page_size.
        The index is the starting index of the current page. The page_size is the number of items required in the current page.
        The data is a list of lists containing the data for the specified page. The next_index is the index of the next page.
        If the next_index is None, it means there are no more pages.
        
        :param index: An integer representing the starting index of the current page. Defaults to None.
        :param page_size: An integer representing the number of items required in the current page. Defaults to 10.
        :return: A dictionary containing the index, data, page_size, and next_index.
        :rtype: dict
        """
       
        focus = []
        dataset = self.indexed_dataset()
        index = 0 if index is None else index
        keys = sorted(dataset.keys())
        assert index >= 0 and index <= keys[-1]
        [focus.append(i)
         for i in keys if i >= index and len(focus) <= page_size]
        data = [dataset[v] for v in focus[:-1]]
        next_index = focus[-1] if len(focus) - page_size == 1 else None
        return {'index': index, 'data': data,
                'page_size': len(data), 'next_index': next_index}
