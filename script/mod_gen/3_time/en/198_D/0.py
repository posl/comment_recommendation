def solve(s1, s2, s3):
    if len(s1) < len(s3):
        s1, s3 = s3, s1
    if len(s2) < len(s3):
        s2, s3 = s3, s2
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    if len(s1) < len(s3):
        s1, s3 = s3, s1
    if len(s2) < len(s3):
        s2, s3 = s3, s2
    s = set(s1+s2+s3)
    if len(s) > 10:
        return 'UNSOLVABLE'
    l = len(s1)
    for i in range(10**l):
        d = {}
        for j, c in enumerate(s1):
            d[c] = i // 10**(l-1-j) % 10
        if d[s1[0]] == 0 or d[s2[0]] == 0 or d[s3[0]] == 0:
            continue
        a = 0
        for c in s1:
            a = 10*a + d[c]
        b = 0
        for c in s2:
            b = 10*b + d[c]
        c = 0
        for c in s3:
            c = 10*c + d[c]
        if a + b == c:
            return f'{a}
{b}
{c}'
    return 'UNSOLVABLE'

if __name__ == '__main__':
    solve()