def main():
    N = int(input())
    # dp[i][j][k] := i 桁目まで決めたときに、
    # その桁の数が j であるような数の個数
    # k = 0 ならば前の桁との差が 1 以下であるような数
    # k = 1 ならばそうでない数
    dp = [[[0] * 2 for _ in range(10)] for _ in range(N + 1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(10):
            for k in range(2):
                for d in range(10):
                    if k == 0:
                        if abs(j - d) <= 1:
                            dp[i + 1][d][0] += dp[i][j][k]
                        else:
                            dp[i + 1][d][1] += dp[i][j][k]
                    else:
                        dp[i + 1][d][1] += dp[i][j][k]
    ans = 0
    for j in range(1, 10):
        ans += dp[N][j][0] + dp[N][j][1]
    print(ans % 998244353)

if __name__ == '__main__':
    main()