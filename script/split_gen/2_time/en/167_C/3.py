def solve():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    ans = 10**9
    for i in range(1<<N):
        cost = 0
        level = [0]*M
        for j in range(N):
            if (i>>j)&1:
                cost += C[j]
                for k in range(M):
                    level[k] += A[j][k]
        if min(level) >= X:
            ans = min(ans, cost)
    if ans == 10**9:
        print(-1)
    else:
        print(ans)
