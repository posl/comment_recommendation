def solve(s1, s2, s3):
    chars = set(s1 + s2 + s3)
    if len(chars) > 10:
        return 'UNSOLVABLE'
    chars = list(chars)
    for perm in permutations(range(10), len(chars)):
        table = {c: str(perm[i]) for i, c in enumerate(chars)}
        if table[s1[0]] == '0' or table[s2[0]] == '0' or table[s3[0]] == '0':
            continue
        n1 = int(''.join([table[c] for c in s1]))
        n2 = int(''.join([table[c] for c in s2]))
        n3 = int(''.join([table[c] for c in s3]))
        if n1 + n2 == n3:
            return '\n'.join([str(n1), str(n2), str(n3)])
    return 'UNSOLVABLE'
