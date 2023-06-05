def solve():
    A, B = map(int, input().split())
    if A <= B:
        print(A + 1)
        return
    l = 0
    r = 1e18
    while r - l > 1:
        m = (l + r) // 2
        if m * (m + 1) // 2 + A // (m + 1) >= B:
            r = m
        else:
            l = m
    print(r + A // (r + 1))
