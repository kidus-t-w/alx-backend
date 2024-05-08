#!/usr/bin/env python3
"""
Basic caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basic caching system"""
    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            pass

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
