#!/usr/bin/env python3
"""
This module defines the MRUCache class, which inherits from BaseCaching and
implements a Most Recently Used (MRU) caching system.
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching and implements MRU caching.
    """

    def __init__(self):
        """
        Initialize the MRUCache class.
        """
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """
        Add an item to the cache using MRU eviction policy.

        Args:
            key (str): The key to associate with the item.
            item: The item to be cached.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage.remove(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard_key = self.usage.pop()
            del self.cache_data[discard_key]
            print(f"DISCARD: {discard_key}")

        self.usage.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key (str): The key associated with the item.

        Returns:
            The cached item, or None if the key is not found.
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage.remove(key)
        self.usage.append(key)
        return self.cache_data[key]
