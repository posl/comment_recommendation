def solve(s1, s2, s3):
    chars = list(set(s1 + s2 + s3))
    if len(chars) > 10:
        return None
    chars.sort()
    for p in permutations(range(10), len(chars)):
        if p[0] == 0:
            continue
        d = dict(zip(chars, p))
        n1 = int(''.join(map(str, [d[c] for c in s1])))
        n2 = int(''.join(map(str, [d[c] for c in s2])))
        n3 = int(''.join(map(str, [d[c] for c in s3])))
        if n1 + n2 == n3:
            return n1, n2, n3
    return None
from itertools import permutations
s1 = input()
s2 = input()
s3 = input()
ans = solve(s1, s2, s3)

if __name__ == '__main__':
    solve()