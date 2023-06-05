def get_input():
    n, m = map(int, input().split())
    p = [0] * m
    s = [0] * m
    for i in range(m):
        p[i], s[i] = input().split()
        p[i] = int(p[i])
    return n, m, p, s
