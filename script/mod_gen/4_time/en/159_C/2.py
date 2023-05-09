def calc_max_volume(L):
    """
    >>> calc_max_volume(3)
    1.0
    >>> calc_max_volume(999)
    36926037.0
    """
    return (L/3)**3 if L%3==0 else (L/3+1)*(L/3)**2

if __name__ == '__main__':
    calc_max_volume()