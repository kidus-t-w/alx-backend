#!/usr/bin/env python3
"""Last-In First-Out caching module.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Last-In First-Out (LIFO) caching system.

    This class implements a Last-In First-Out (LIFO) caching system. It keeps
    track of the most recently used items in the cache. When the cache is full,
    the least recently used item is discarded to make room for the new item.

    It is a subclass of BaseCaching, so it inherits its constants and methods
    (print_cache, get, put).
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache.
            Removes the oldest item in the cache
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
