def solve():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[[False for _ in range(301)] for _ in range(301)] for _ in range(301)]
    dp[0][0][0] = True
    for i in range(N):
        for a in range(301):
            for b in range(301):
                if dp[i][a][b]:
                    dp[i+1][a][b] = True
                    if a + A[i] <= 300 and b + B[i] <= 300:
                        dp[i+1][a+A[i]][b+B[i]] = True
    ans = -1
    for i in range(301):
        for j in range(301):
            if dp[N][i][j] and (i >= X and j >= Y):
                if ans == -1:
                    ans = i + j
                else:
                    ans = min(ans, i+j)
    print(ans)
solve()
