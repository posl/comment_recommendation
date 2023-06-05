def solve():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    #print(N, K, R, S, P, T)
    #dp[i][j]表示前i轮，第i轮使用了j手的最大得分
    #第i轮使用了j手，第i-1轮使用了k手，k!=j, k属于[1, 2, 3]，取最大值
    #dp[i][j] = max(dp[i-1][k] + score(i, j))
    #dp[0][j] = 0
    #score(i, j)表示第i轮使用了j手的得分
    #score(i, j) = R if j == 1
    #score(i, j) = S if j == 2
    #score(i, j) = P if j == 3
    #score(i, j) = 0 if j == 0
    dp = [[0 for _ in range(4)] for _ in range(N+1)]
    score = [0, R, S, P]
    for i in range(1, N+1):
        for j in range(1, 4):
            dp[i][j] = max(dp[i-1][k] + score[j] for k in range(1, 4) if k != j)
        if T[i-1] == 'r':
            dp[i][1] = max(dp[i][1], dp[i-1][0] + score[1])
        elif T[i-1] == 's':
            dp[i][2] = max(dp[i][2], dp[i-1][0] + score[2])
        elif T[i-1] == 'p':
            dp[i][3] = max(dp[i][3], dp[i-1][0] + score[3])
    ans = max(dp[N][1], dp[N][2], dp[N][3])
    print(ans)
    return 0
solve()
