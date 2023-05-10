def solve():
    A, B, C = map(int, input().split())
    dp = [[[0.0 for _ in range(101)] for _ in range(101)] for _ in range(101)]
    for a in range(100, -1, -1):
        for b in range(100, -1, -1):
            for c in range(100, -1, -1):
                if a == 100 or b == 100 or c == 100:
                    continue
                if a + b + c == 0:
                    continue
                dp[a][b][c] = (
                    (dp[a + 1][b][c] * a + dp[a][b + 1][c] * b + dp[a][b][c + 1] * c + 100) / (a + b + c)
                )
    return dp[A][B][C]
print(solve())

if __name__ == '__main__':
    solve()