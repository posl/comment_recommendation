def kth_smallest_permutation(s, k):
    from math import factorial
    from collections import Counter
    from itertools import permutations
    n = len(s)
    c = Counter(s)
    d = factorial(n)
    for v in c.values():
        d //= factorial(v)
    if k > d:
        return None
    for p in permutations(sorted(s)):
        if k == 1:
            return ''.join(p)
        k -= 1
    return None
