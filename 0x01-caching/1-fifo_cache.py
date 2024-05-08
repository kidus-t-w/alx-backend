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
            if key in self.cache_data and self.cache_data[key] != item:
                self.cache_data[key] = item

            elif (len(self.cache_data) == BaseCaching.MAX_ITEMS):
                key_to_remove = list(self.cache_data.keys())[0]
                self.cache_data.pop(key_to_remove)
                print("DISCARD:{}".format(key_to_remove))
            self.cache_data[key] = item

    def get(self, key):
        """
        Return item form the cache
        """
        if key is None and key not in self.cache_data:
            return None
        if key in self.cache_data:
            return self.cache_data[key]
