#!/usr/bin/env python3
"""First-In First-Out caching module.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.

        If the key or item is None, this method does nothing.

        If the cache is full, the oldest item is removed from the cache
        and a message is printed indicating which key was removed.

        Args:
            key (object): The key used to store the item.
            item (object): The item to store in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)  # noqa: T001

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
