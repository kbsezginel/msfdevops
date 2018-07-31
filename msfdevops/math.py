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
    # Check that user passes list
    if isinstance(num_list, list):
        raise TypeError('Input must be type list')

    # Check that list has length
    if len(num_list) == 0:
        raise ZeroDivisionError('Cannot calulate mean of empty list')

    try:
        avg = sum(num_list) / len(num_list)
    except TypeError:
        raise TypeError('Values of list must be type int or float')
    return avg
