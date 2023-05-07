def solve(n, x, s):
    p = [0] * (n + 1)
    p[0] = x
    for i in range(n):
        if s[i] == 'U':
            p[i + 1] = p[i] // 2
        elif s[i] == 'L':
            p[i + 1] = p[i] * 2 - 1
        else:
            p[i + 1] = p[i] * 2 + 1
    return p[-1]
