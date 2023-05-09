def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    l = 0
    r = 1000000000000
    while r - l > 0.0000000000001:
        m = (l + r) / 2
        t = 0
        for i in range(N):
            t += max(0, A[i] - m / B[i])
        if t >= m:
            l = m
        else:
            r = m
    print(l)
solve()
