def main():
    N = int(input())
    A = [[int(i) for i in input().split()] for _ in range(N)]
    dp = [[0] * 5 for _ in range(N + 1)]
    for i in range(N):
        for j in range(5):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if A[i][0] - A[i][1] == i:
                dp[i + 1][A[i][1]] = max(dp[i + 1][A[i][1]], dp[i][j] + A[i][2])
            if A[i][0] == i:
                dp[i + 1][A[i][1]] = max(dp[i + 1][A[i][1]], dp[i][j] + A[i][2], dp[i][j - 1] + A[i][2])
    print(max(dp[-1]))
