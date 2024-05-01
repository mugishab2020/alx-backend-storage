#!/usr/bin/env python3
'''this function the function for Writing strings to Redis'''


import redis
import uuid
from functools import wraps
from typing import Union, Callable


def replay(method: callable) -> None:
    '''replay function history of calls of a particular function.'''
    m = redis.Redis()
    key = method.__qualname__
    input = key + ":inputs"
    output = key + ":outputs"
    calls_n = m.get(key)
    inputs = m.lrange(input, 0, -1)
    outputs = m.lrange(output, 0, -1)
    my_list = zip(inputs, outputs)
    print(f"{key} was called {calls_n.decode('utf-8')} times:")
    for tup in my_list:
        first = tup[0].decode('utf-8')
        last = tup[1].decode('utf-8')
        print(f"{key}(*{first}) -> {last}")


def call_history(method: Callable) -> Callable:
    '''function for making call history'''
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper_hist(self, *args, **kwargs):
        '''Wrapper for pushing the resultds the the redis lists'''
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data

    return wrapper_hist


def count_calls(method: Callable) -> Callable:
    '''function to count the number of calls to a method'''
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> None:
        '''returns the number of calls'''
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str,
                                                          bytes, int, None]:
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        return self.get(key, fn=int)
