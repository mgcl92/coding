def equilibrium_index(arr: list[int]) -> list:
    """
    Find the equilibrium index of an array.

    :param arr: an array comprised by integers
    :return: -1 or the equilibrium index of arr
    """
    total = sum(arr)
    left = 0

    for i, val in arr:
        total -= val
        if left == total:
            return i
        left += val

    return -1


