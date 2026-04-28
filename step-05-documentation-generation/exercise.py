def chunk_list(values: list[int], size: int) -> list[list[int]]:
    """Split a list of integers into chunks of a fixed size.

    Parameters:

        values: The list of integers to split.

        size: The maximum number of items in each chunk. Must be greater than 0.

    Returns:

        A list of chunks. Each chunk is a list of integers.

    Example:

        >>> chunk_list([1, 2, 3, 4, 5], 2)

        [[1, 2], [3, 4], [5]]

    """
    if size <= 0:
        raise ValueError("size must be > 0")
    return [values[index : index + size] for index in range(0, len(values), size)]


def moving_average(values: list[float], window: int) -> list[float]:
    """Calculate moving averages over a fixed-size sliding window.

    Args:
        values: The list of numbers to average.
        window: The number of items in each moving window. Must be greater than 0.

    Returns:
        A list of averages. Returns an empty list when the window is larger than the input.

    Example:
        >>> moving_average([10.0, 20.0, 30.0], 2)
        [15.0, 25.0]
    """
    if window <= 0:
        raise ValueError("window must be > 0")
    if window > len(values):
        return []
    result: list[float] = []
    for index in range(len(values) - window + 1):
        current = values[index : index + window]
        result.append(sum(current) / window)
    return result