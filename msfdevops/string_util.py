"""
Miscellaneous string functions.
"""


def title_string(s):
    """
    Converts a string to title case.

    Title case means that the first character of every word is capitalized, otherwise lowercase.

    Parameters
    ----------
    s: string
        The string to convert to title case

    Returns
    -------
    str
        The input string in title case

    Examples
    --------
    >>> title_string("this iS a StrING to be ConverTeD")
    'This Is A String To Be Converted'
    """
    if not isinstance(s, str):
        raise TypeError('Input must be type string')

    if len(s) == 0:
        return ''

    new_str = s[0].upper()
    for i in range(1, len(s)):
        if s[i - 1] == ' ':
            new_str += s[i].upper()
        else:
            new_str += s[i].lower()
    return new_str
