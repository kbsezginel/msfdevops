"""
Math operations.
"""


def mean(num_list):
    """
    Calculate the man of a list of numbers

    Parameters
    ----------
    num_list: list
        The list to take average of

    Returns
    -------
    avg: float
        The mean of a list

    Examples
    --------

    >>> mean([1, 2, 3, 4, 5])
    3.0
    """

    avg = sum(num_list) / len(num_list)
    return avg
