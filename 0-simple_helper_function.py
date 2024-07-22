#!/usr/bin/env python3
"""
This module contains a helper function for calculating
the start and end indices
for pagination based on a given page number and page size.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Args:
        page (int): the current page number (1-indexed)
        page_size (int): the number of items per page

    Returns:
        Tuple[int, int]: a tuple containing the start index and the end index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
