def main():
    N = int(input())
    snukes = []
    for _ in range(N):
        T, X, A = map(int, input().split())
        snukes.append((T, X, A))
    snukes.sort()
    dp = [[0 for _ in range(5)] for _ in range(N+1)]
    for i in range(N):
        T, X, A = snukes[i]
        for j in range(5):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j == X:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j] + A)
            if j < X:
                dp[i+1][X] = max(dp[i+1][X], dp[i][j] + A)
            if j > X:
                dp[i+1][X] = max(dp[i+1][X], dp[i][j] + A)
    print(max(dp[-1]))
