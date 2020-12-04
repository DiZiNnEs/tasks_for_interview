from functools import reduce


def count_multipliers(*args) -> int:
    return reduce((lambda x, y: x * y), args)
