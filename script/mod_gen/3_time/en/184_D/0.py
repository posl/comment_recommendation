def main():
    A, B, C = map(int, input().split())
    dp = [[[0 for _ in range(100)] for _ in range(100)] for _ in range(100)]
    dp[A][B][C] = 1
    for a in range(100):
        for b in range(100):
            for c in range(100):
                if a == 0 and b == 0 and c == 0:
                    continue
                total = a + b + c
                dp[a][b][c] += a / total * dp[max(0, a - 1)][b][c]
                dp[a][b][c] += b / total * dp[a][max(0, b - 1)][c]
                dp[a][b][c] += c / total * dp[a][b][max(0, c - 1)]
                dp[a][b][c] *= total / (total + 1)
                dp[a][b][c] += 1
    ans = 0
    for a in range(100):
        for b in range(100):
            for c in range(100):
                if a == 0 and b == 0 and c == 0:
                    continue
                total = a + b + c
                ans += dp[a][b][c] * a / total
                ans += dp[a][b][c] * b / total
                ans += dp[a][b][c] * c / total
    print(ans)

if __name__ == '__main__':
    main()