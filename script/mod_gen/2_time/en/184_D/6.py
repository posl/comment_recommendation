def main():
    A, B, C = list(map(int, input().split()))
    dp = [[[0 for _ in range(100)] for _ in range(100)] for _ in range(100)]
    for a in range(99):
        for b in range(99):
            for c in range(99):
                dp[a][b][c] = 1 + (dp[a+1][b][c] * a + dp[a][b+1][c] * b + dp[a][b][c+1] * c) / (a + b + c)
    print(dp[A][B][C])
main()
