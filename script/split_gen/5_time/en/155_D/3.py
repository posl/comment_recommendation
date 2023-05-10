def solve(N, K, A):
    A.sort()
    l = -10**18
    r = 10**18
    while l + 1 < r:
        m = (l + r) // 2
        cnt = 0
        for i in range(N):
            if A[i] < 0:
                cnt += N - bisect.bisect_left(A, m // A[i])
            elif A[i] > 0:
                cnt += bisect.bisect_right(A, m // A[i])
            else:
                if m >= 0:
                    cnt += N
        cnt //= 2
        if cnt >= K:
            r = m
        else:
            l = m
    return r
