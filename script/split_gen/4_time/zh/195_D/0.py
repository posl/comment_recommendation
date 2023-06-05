def solve():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = list(map(int, input().split()))
    for _ in range(Q):
        L, R = map(int, input().split())
        L -= 1
        R -= 1
        ans = 0
        for bit in range(1 << (R - L + 1)):
            w = 0
            v = 0
            for i in range(R - L + 1):
                if bit & (1 << i):
                    w += W[L + i]
                    v += V[L + i]
            for i in range(M):
                if w <= X[i]:
                    ans = max(ans, v)
        print(ans)
