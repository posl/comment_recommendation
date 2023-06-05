def main():
    S = int(input())
    mod = 10**9 + 7
    dp = [[0]*(S+1) for _ in range(S+1)]
    dp[0][0] = 1
    for i in range(3, S+1):
        for j in range(S+1):
            for k in range(S+1):
                if j + i <= S:
                    dp[j+i][i] += dp[j][k]
                    dp[j+i][i] %= mod
    ans = 0
    for i in range(1, S+1):
        ans += dp[S][i]
        ans %= mod
    print(ans)
