def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(list(map(int, input().split())))
    S = sorted(S, key=lambda x: x[0])
    dp = [[0] * 5 for i in range(N)]
    for i in range(N):
        for j in range(5):
            if S[i][1] == j:
                dp[i][j] = S[i][2]
            else:
                dp[i][j] = 0
    for i in range(1, N):
        for j in range(5):
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
        for j in range(5):
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + S[i][2])
        for j in range(5):
            if S[i][1] == j:
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + S[i][2])
            else:
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
    print(max(dp[N - 1]))
