#!/usr/bin/env python3
"""
MRU cache system.
"""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Most Recently Used caching system."""
    def __init__(self):
        """Initlize"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data and item is None:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                removed, _ = self.cache_data.popitem(True)
                print("DESTROYED:", removed)
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item form the cache by a key
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
            return self.cache_data.get(key, None)
