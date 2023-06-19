def solve(s1, s2, s3):
    s = set(s1 + s2 + s3)
    if len(s) > 10:
        return False
    chars = tuple(s)
    n = len(chars)
    if n > 10:
        return False
    for perm in permutations(range(10), n):
        d = dict(zip(chars, perm))
        if any(d[s[0]] == 0 for s in (s1, s2, s3)):
            continue
        n1 = int(''.join(str(d[c]) for c in s1))
        n2 = int(''.join(str(d[c]) for c in s2))
        n3 = int(''.join(str(d[c]) for c in s3))
        if n1 + n2 == n3:
            return n1, n2, n3
    return False
from itertools import permutations
s1 = input()
s2 = input()
s3 = input()
ans = solve(s1, s2, s3)
