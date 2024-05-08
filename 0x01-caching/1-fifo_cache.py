#!/usr/bin/env python3
"""
FIFO cache system
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def put(self, key, item):
        """
        Add item in the cache
        """
        if key is not None and item is not None:
            if (len(self.cache_data) == super.MAX_ITEMS):
                self.cache_data.popitem()
                print("DISCARD:{}".format(self.key))
            self.cache_data[key] = item

    def get(self, key):
        """
        Return item form the cache
        """
        if key is not self.cache_data and key in self.cache_data:
            return self.cache_data[key]
