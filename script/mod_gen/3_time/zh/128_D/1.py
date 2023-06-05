def main():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    # dp[i][j][l]表示前i个珠宝，操作j次，手中有l个珠宝时的最大值
    dp = [[[float('-inf') for _ in range(n+1)] for _ in range(k+1)] for _ in range(n+1)]
    dp[0][0][0] = 0
    for i in range(1, n+1):
        for j in range(k+1):
            for l in range(n+1):
                # 操作A
                if l >= 1:
                    dp[i][j][l] = dp[i-1][j][l-1]
                # 操作B
                if l < n:
                    dp[i][j][l] = max(dp[i][j][l], dp[i-1][j][l+1])
                # 操作C
                if j >= 1:
                    dp[i][j][l] = max(dp[i][j][l], dp[i-1][j-1][l] + values[i-1])
                # 操作D
                if j >= 1 and l < n:
                    dp[i][j][l] = max(dp[i][j][l], dp[i-1][j-1][l+1] + values[i-1])
    ans = 0
    for j in range(k+1):
        for l in range(n+1):
            ans = max(ans, dp[n][j][l])
    print(ans)

if __name__ == '__main__':
    main()