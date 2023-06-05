def solve():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    ans = float("inf")
    for i in range(2**N):
        cost = 0
        understand = [0 for _ in range(M)]
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    understand[k] += A[j][k]
        if all(understand[k] >= X for k in range(M)):
            ans = min(ans, cost)
    if ans == float("inf"):
        print(-1)
    else:
        print(ans)
solve()
