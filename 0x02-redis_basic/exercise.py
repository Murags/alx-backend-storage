#!/usr/bin/env python3
"""creates a cache"""


import redis
import uuid
from typing import Union


class Cache:
    """_summary_
    """
    def __init__(self):
        """_summary_
        """
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """_summary_

        Args:
            data (Union[str, bytes, int, float]): _description_

        Returns:
            str: _description_
        """
        key = str(uuid.uuid4())

        if isinstance(data, (str, bytes, int, float)):
            self._redis.set(key, data)

        return key
