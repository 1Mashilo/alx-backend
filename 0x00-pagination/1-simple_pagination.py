#!/usr/bin/env python3
"""
This module contains a Server class to paginate a dataset of popular baby names
from a CSV file. It also includes the index_range helper function to calculate
the start and end indices for pagination.
"""

import csv
from typing import List, Tuple

class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
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

    def dataset(self) -> List[List]:
        """Cached dataset

        Returns:
            List[List]: the cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of data from the dataset

        Args:
            page (int): the current page number (1-indexed)
            page_size (int): the number of items per page

        Returns:
            List[List]: a list of rows from the dataset for the specified page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = self.index_range(page, page_size)
        dataset = self.dataset()
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

