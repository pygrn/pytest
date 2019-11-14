import math


def gigabytes2bytes(size_gigabytes: int) -> int:
    """
    >>> gigabytes2bytes(30)
    32212254720
    """
    if size_gigabytes < 0:
        raise Exception("gigabytes should be positive")
    p = math.pow(1024, 3)
    s = round(size_gigabytes * p, 2)
    return int(s)
