def solve():
    A, B, C = map(int, input().split())
    dp = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]
    dp[A][B][C] = 0
    for a in range(A, 100):
        for b in range(B, 100):
            for c in range(C, 100):
                if a == 99 and b == 99 and c == 99:
                    continue
                dp[a+1][b][c] += dp[a][b][c] * a / (a+b+c)
                dp[a][b+1][c] += dp[a][b][c] * b / (a+b+c)
                dp[a][b][c+1] += dp[a][b][c] * c / (a+b+c)
                dp[a][b][c] += 1
    print(dp[99][99][99])

if __name__ == '__main__':
    solve()