def main():
    N = int(input())
    S = []
    for _ in range(N):
        S.append(list(map(int, input().split())))
    S = sorted(S, key=lambda x: x[0])
    dp = [[0 for _ in range(5)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(5):
            dp[i][j] = max(dp[i][j], dp[i-1][j])
            if j == S[i-1][1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + S[i-1][2])
            else:
                dp[i][j] = max(dp[i][j], dp[i-1][S[i-1][1]] + S[i-1][2])
    print(max(dp[N]))
