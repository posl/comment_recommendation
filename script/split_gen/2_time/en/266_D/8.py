def main():
    N = int(input())
    S = [list(map(int, input().split())) for i in range(N)]
    dp = [[0] * 5 for i in range(N + 1)]
    for i in range(N):
        for j in range(5):
            dp[i + 1][j] = dp[i][j]
        dp[i + 1][S[i][1]] = max(dp[i + 1][S[i][1]], dp[i][S[i][1]])
        for j in range(5):
            if j == S[i][1]:
                continue
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + S[i][2] * (S[i][0] - i))
    print(max(dp[N]))
