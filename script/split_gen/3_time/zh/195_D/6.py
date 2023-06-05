def solve():
    N, M, Q = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    Query = [list(map(int, input().split())) for _ in range(Q)]
    for L, R in Query:
        ans = 0
        for i in range(M):
            if i < L-1 or R-1 < i:
                ans += X[i]
        ans = 0
        for i in range(N):
            if i < L-1 or R-1 < i:
                ans += X[i]
        print(ans)
