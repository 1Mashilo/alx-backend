#!/usr/bin/env python3
"""
This module defines the FIFOCache class, which inherits from BaseCaching and
implements a FIFO caching system.
"""


from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """
    FIFOCache class inherits from BaseCaching and implements a FIFO caching
    system.
    """

    def __init__(self):
        """
        Initialize the FIFOCache class.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item to the cache using FIFO eviction policy.

        Args:
            key (str): The key to associate with the item.
            item: The item to be cached.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key (str): The key associated with the item.

        Returns:
            The cached item, or None if the key is not found.
        """
        return self.cache_data.get(key, None)
