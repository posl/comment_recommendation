def main():
    N = int(input())
    MOD = 998244353
    #dp[i][j] := i桁の数字で、最大値がjのものの個数
    dp = [[0 for j in range(10)] for i in range(19)]
    for i in range(1, 10):
        dp[1][i] = 1
    for i in range(2, 19):
        for j in range(1, 10):
            for k in range(1, j+1):
                dp[i][j] += dp[i-1][k]
                dp[i][j] %= MOD
    ans = 0
    for i in range(1, 19):
        for j in range(1, 10):
            ans += dp[i][j]
            ans %= MOD
    N += 1
    for i in range(1, 19):
        if N < 10**i:
            break
        for j in range(1, 10):
            ans += dp[i][j]
            ans %= MOD
    s = str(N)
    for i in range(1, len(s)):
        for j in range(1, 10):
            ans += dp[i][j]
            ans %= MOD
    for i in range(1, int(s[0])):
        for j in range(1, 10):
            if i > j:
                continue
            ans += dp[len(s)][j]
            ans %= MOD
    for i in range(1, len(s)):
        for j in range(1, int(s[i])):
            if int(s[i-1]) > j:
                continue
            ans += dp[len(s)-i][j]
            ans %= MOD
    print(ans)
