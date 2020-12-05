from functools import reduce


def get_multiply(result_from_post_response: list[int]) -> int:
    return reduce((lambda x, y: x * y), result_from_post_response)
