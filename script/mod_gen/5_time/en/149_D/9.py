def solve():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    # dp[i][j] = i回戦までの最大得点。j=0: r, j=1: s, j=2: p
    dp = [[0] * 3 for _ in range(N+1)]
    for i in range(N):
        if T[i] == 'r':
            dp[i+1][0] = max(dp[i][1], dp[i][2]) + P
            dp[i+1][1] = max(dp[i][0], dp[i][2])
            dp[i+1][2] = max(dp[i][0], dp[i][1])
        elif T[i] == 's':
            dp[i+1][0] = max(dp[i][1], dp[i][2])
            dp[i+1][1] = max(dp[i][0], dp[i][2]) + R
            dp[i+1][2] = max(dp[i][0], dp[i][1])
        else:
            dp[i+1][0] = max(dp[i][1], dp[i][2])
            dp[i+1][1] = max(dp[i][0], dp[i][2])
            dp[i+1][2] = max(dp[i][0], dp[i][1]) + S
        if i >= K:
            if T[i-K] == 'r':
                dp[i+1][0] = max(dp[i+1][0], dp[i-K][0])
            elif T[i-K] == 's':
                dp[i+1][1] = max(dp[i+1][1], dp[i-K][1])
            else:
                dp[i+1][2] = max(dp[i+1][2], dp[i-K][2])
    print(max(dp[N]))

if __name__ == '__main__':
    solve()