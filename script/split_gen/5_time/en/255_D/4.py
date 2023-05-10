def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    s = [0] * (N + 1)
    for i in range(N):
        s[i + 1] = s[i] + A[i]
    for x in X:
        l = -1
        r = N
        while r - l > 1:
            m = (l + r) // 2
            if A[m] >= x:
                r = m
            else:
                l = m
        ans = 0
        if r > 0:
            ans += x * r - s[r]
        if r < N:
            ans += s[N] - s[r] - x * (N - r)
        print(ans)
