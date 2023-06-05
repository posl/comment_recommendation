def solve():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[[0 for i in range(300 * 300 + 1)] for i in range(300 + 1)] for i in range(N + 1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(300):
            for k in range(300 * 300 + 1):
                if dp[i][j][k] == 1:
                    dp[i + 1][j][k] = 1
                    if j + 1 <= 300:
                        dp[i + 1][j + 1][k + A[i]] = 1
    ans = -1
    for i in range(300 * 300 + 1):
        if dp[N][X][i] == 1 and dp[N][Y][i] == 1:
            ans = i
            break
    print(ans)
solve()
