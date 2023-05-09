def get_primes(n):
    """Return a list of prime numbers less than or equal to n."""
    if n < 2:
        return []
    if n == 2:
        return [2]
    # do only odd numbers starting at 3
    s = range(3, n + 1, 2)
    # n**0.5 may be slightly faster than math.sqrt(n)
    mroot = n ** 0.5
    half = len(s)
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = (m * m - 3) / 2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i = i + 1
        m = 2 * i + 3
    # make exception for 2
    return [2] + [x for x in s if x]
