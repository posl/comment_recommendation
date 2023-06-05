def solve(s1, s2, s3):
    chars = set(s1 + s2 + s3)
    if len(chars) > 10:
        return False
    chars = list(chars)
    chars.sort()
    for perm in permutations(range(10), len(chars)):
        if 0 in perm[:len(chars) - 1]:
            continue
        d = dict(zip(chars, perm))
        n1 = int(''.join(map(str, [d[c] for c in s1])))
        n2 = int(''.join(map(str, [d[c] for c in s2])))
        n3 = int(''.join(map(str, [d[c] for c in s3])))
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return True
    return False
