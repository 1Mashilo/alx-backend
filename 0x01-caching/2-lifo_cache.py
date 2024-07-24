#!/usr/bin/env python3
"""
This module defines the LIFOCache class, which inherits from BaseCaching and
implements a LIFO caching system.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching and implements LIFO caching.
    """

    def __init__(self):
        """
        Initialize the LIFOCache class.
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Add an item to the cache using LIFO eviction policy.

        Args:
            key (str): The key to associate with the item.
            item: The item to be cached.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.stack.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard_key = self.stack.pop()
                del self.cache_data[discard_key]
                print(f"DISCARD: {discard_key}")
            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key (str): The key associated with the item.

        Returns:
            The cached item, or None if the key is not found.
        """
        return self.cache_data.get(key, None)
