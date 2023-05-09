def calc(n, p, q):
    from itertools import permutations
    perm = list(permutations(range(1, n + 1)))
    return abs(perm.index(tuple(p)) - perm.index(tuple(q)))
