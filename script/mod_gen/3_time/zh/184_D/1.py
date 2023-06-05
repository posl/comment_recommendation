def solve():
    A, B, C = map(int, input().split())
    dp = [[[0] * 101 for _ in range(101)] for _ in range(101)]
    for i in range(100, A - 1, -1):
        for j in range(100, B - 1, -1):
            for k in range(100, C - 1, -1):
                dp[i][j][k] = (i * dp[i + 1][j][k] + j * dp[i][j + 1][k] + k * dp[i][j][k + 1] + 300) / (i + j + k)
    print(dp[A][B][C])

if __name__ == '__main__':
    solve()