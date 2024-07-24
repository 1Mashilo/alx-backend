#!/usr/bin/env python3
"""
This module defines the BasicCache class, which inherits from BaseCaching and
implements a basic caching system without any eviction policy.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class inherits from BaseCaching and provides a simple
    implementation of a caching system.
    """

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key (str): The key to associate with the item.
            item: The item to be cached.
        """
        if key is not None and item is not None:
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
        return self.cache_data[key]
