#!/usr/bin/env python3
"""
Basic caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basic caching system"""
    def get(self, key: str) -> Optional[Any]:
        """ Get an item by key

        Args:
            key (str): key of the item to retrieve

        Returns:
            Optional[Any]: item retrieved from the
              cache or None if not found
        """
        return self.cache_data.get(key)

    def put(self, key: str, item: Any) -> None:
        """ Add an item in the cache

        Args:
            key (str): key of the item to add
            item (Any): item to add

        Returns:
            None
        """
        if key is None:
            return None
        self.cache_data[key] = item
