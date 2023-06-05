def max_rainy_days(s):
    """
    >>> max_rainy_days('RRS')
    2
    >>> max_rainy_days('SSS')
    0
    >>> max_rainy_days('RSR')
    1
    """
    return s.count('R')
