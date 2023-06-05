def solve():
    N, M, Q = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    query = [list(map(int, input().split())) for _ in range(Q)]
    ans = []
    for q in query:
        L, R = q[0], q[1]
        X_ = X[:L-1] + X[R:]
        X_.sort()
        ans.append(calc(X_, WV))
    for a in ans:
        print(a)
