def solve(l):
    n = 20
    m = 60
    ans = []
    for i in range(1, n):
        ans.append((i, i+1, 0))
    ans.append((1, n, 1))
    ans.append((n, 1, 1))
    m -= 2
    for i in range(1, n-1):
        ans.append((i, i+2, 1))
        m -= 1
    for i in range(1, n-1):
        ans.append((i, n, 1))
        m -= 1
    for i in range(1, n-1):
        ans.append((i, n, 2))
        m -= 1
    ans.append((1, n, l-1))
    m -= 1
    ans.append((1, n, l))
    m -= 1
    ans.append((1, n, l+1))
    m -= 1
    for i in range(1, n-1):
        ans.append((i, n, l+2))
        m -= 1
    for i in range(1, n-1):
        ans.append((i, n, l+3))
        m -= 1
    for i in range(1, n-1):
        ans.append((i, n, l+4))
        m -= 1
    for i in range(1, n-1):
        ans.append((i, n, l+5))
        m -= 1
    for i in range(1, n-1):
        ans.append((i, n, l+6))
        m -= 1
    for i in range(1, n-1):
        ans.append((i, n, l+7))
        m -= 1
    for i in range(1, n-1):
        ans.append((i, n, l+8))
        m -= 1
    for i in range(1, n-1):
        ans.append((i, n, l+9))
        m -= 1
    for i in range(1, n-1):
        ans.append((i, n, l+10))
        m -= 1
    for i in range(1, n-1):
        ans.append((i,
