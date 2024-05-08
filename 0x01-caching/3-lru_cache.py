#!/usr/bin/env python3
"""
LRU cache system
"""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Least Recently Used caching system
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is None or item is None:
            return
        if key not in self.cache_data and item is not None:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                removed, _ = self.cache_data.popitem(False)
                print("DISCARD:", removed)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key"""
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key, None)
        else:
            return None
