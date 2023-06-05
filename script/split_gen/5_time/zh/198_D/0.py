def solve(s1, s2, s3):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s1) > len(s3):
        s1, s3 = s3, s1
    if len(s2) > len(s3):
        s2, s3 = s3, s2
    chars = set(s1 + s2 + s3)
    if len(chars) > 10:
        return False
    char_list = list(chars)
    for perm in permutations(range(10), len(chars)):
        d = dict(zip(char_list, perm))
        if d[s1[0]] == 0 or d[s2[0]] == 0 or d[s3[0]] == 0:
            continue
        n1 = sum(d[c] * (10 ** (len(s1) - i - 1)) for i, c in enumerate(s1))
        n2 = sum(d[c] * (10 ** (len(s2) - i - 1)) for i, c in enumerate(s2))
        n3 = sum(d[c] * (10 ** (len(s3) - i - 1)) for i, c in enumerate(s3))
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return True
    return False
s1 = input()
s2 = input()
s3 = input()
