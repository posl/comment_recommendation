def solve():
    # dp[i][j][k] := i番目までのケーキからj個選んだ時の, 人気度の合計の絶対値の最大値
    dp = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)]
    for i in range(n):
        for j in range(m+1):
            for k in range(2):
                for l in range(2):
                    for o in range(2):
                        if j == 0:
                            dp[l][o][1] = 0
                        else:
                            if k == 0:
                                if o == 0:
                                    dp[l][o][1] = max(dp[l][o][1], dp[l][o][0] + abs(x[i]))
                                else:
                                    dp[l][o][1] = max(dp[l][o][1], dp[l][o][0] + abs(y[i]))
                            else:
                                if o == 0:
                                    dp[l][o][1] = max(dp[l][o][1], dp[l][o][0] - abs(x[i]))
                                else:
                                    dp[l][o][1] = max(dp[l][o][1], dp[l][o][0] - abs(y[i]))
                        dp[l][o][0] = dp[l][o][1]
    print(dp[0][0][1])
    return
