def main():
    A,B,C = map(int, input().split())
    X = A+B+C
    dp = [[[0 for _ in range(X+1)] for _ in range(X+1)] for _ in range(X+1)]
    dp[A][B][C] = 1
    for a in range(X+1):
        for b in range(X+1):
            for c in range(X+1):
                if a+b+c == 0:
                    continue
                dp[a][b][c] *= a+b+c
                if a > 0:
                    dp[a][b][c] += dp[a-1][b][c]*a
                if b > 0:
                    dp[a][b][c] += dp[a+1][b-1][c]*b
                if c > 0:
                    dp[a][b][c] += dp[a][b+1][c-1]*c
                dp[a][b][c] /= a+b+c
    ans = 0
    for a in range(X+1):
        for b in range(X+1):
            for c in range(X+1):
                if a+b+c == 0:
                    continue
                ans += dp[a][b][c]*abs(a-A)
                ans += dp[a][b][c]*abs(b-B)
                ans += dp[a][b][c]*abs(c-C)
    print(ans)

if __name__ == '__main__':
    main()