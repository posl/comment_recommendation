def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    ans = [0 for i in range(10)]
    for i in range(10):
        for j in range(10):
            for k in range(10):
                dp = [[[0 for l in range(10)] for m in range(10)] for o in range(10)]
                dp[i][j][k] = 1
                for l in range(n):
                    dp2 = [[[0 for q in range(10)] for r in range(10)] for s in range(10)]
                    for q in range(10):
                        for r in range(10):
                            for s in range(10):
                                if dp[q][r][s] == 0:
                                    continue
                                if l == n-1:
                                    dp2[(q+a[l])%10][r][s] += dp[q][r][s]
                                    dp2[q][(r+a[l])%10][s] += dp[q][r][s]
                                else:
                                    dp2[(q+a[l])%10][r][s] += dp[q][r][s]
                                    dp2[q][(r+a[l])%10][s] += dp[q][r][s]
                                    dp2[q][r][(s+a[l])%10] += dp[q][r][s]
                                    dp2[(q*a[l])%10][r][s] += dp[q][r][s]
                                    dp2[q][(r*a[l])%10][s] += dp[q][r][s]
                                    dp2[q][r][(s*a[l])%10] += dp[q][r][s]
                    dp = dp2
                ans[k] += dp2[0][0][k]
    for i in range(10):
        print(ans[i]%mod)
