def solve(X, M):
    d = 0
    for c in X:
        d = max(d, int(c))
    if len(X) == 1:
        if int(X) <= M:
            return 1
        else:
            return 0
    l = d
    r = 10 ** 18 + 1
    while r - l > 1:
        m = (l + r) // 2
        if is_ok(X, M, m):
            l = m
        else:
            r = m
    return l - d
