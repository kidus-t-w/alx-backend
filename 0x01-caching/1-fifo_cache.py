#!/usr/bin/env python3
"""
FIFO cache system
"""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache system
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:{}".format(first_key))

    def get(self, key):
        """
        Return item form the cache
        """
        if key is None and key not in self.cache_data:
            return None
        return self.cache_data[key]
