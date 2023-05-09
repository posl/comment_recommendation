def solve():
    N, K = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    L = K
    R = 10**18
    while L + 1 < R:
        M = (L + R) // 2
        cnt = K
        for i in range(N):
            if M >= A[i]:
                cnt += B[i]
        if cnt >= M:
            L = M
        else:
            R = M
    print(L)
