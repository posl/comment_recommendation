def next_permutation(a):
    """Generate the lexicographically next permutation inplace.
    https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
    https://www.nayuki.io/res/next-lexicographical-permutation-algorithm/nextperm.py
    Return false if there is no next permutation.
    """
    # Find non-increasing suffix
    i = len(a) - 1
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    # Find successor to pivot
    j = len(a) - 1
    while a[j] <= a[i - 1]:
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]
    # Reverse suffix
    a[i : ] = a[len(a) - 1 : i - 1 : -1]
    return True
