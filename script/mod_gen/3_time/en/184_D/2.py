def main():
    A,B,C = map(int, input().split())
    dp = [[[0.0 for _ in range(200)] for _ in range(200)] for _ in range(200)]
    dp[A][B][C] = 1.0
    ans = 0.0
    for i in range(A+1):
        for j in range(B+1):
            for k in range(C+1):
                if i+j+k == 0:
                    continue
                if i+j+k == 100:
                    ans += dp[i][j][k]
                    continue
                if i > 0:
                    dp[i-1][j+1][k+1] += dp[i][j][k] * i / (i+j+k)
                if j > 0:
                    dp[i+1][j-1][k+1] += dp[i][j][k] * j / (i+j+k)
                if k > 0:
                    dp[i+1][j+1][k-1] += dp[i][j][k] * k / (i+j+k)
    print(ans)

if __name__ == '__main__':
    main()