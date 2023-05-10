def main():
    S = int(input())
    mod = 10**9 + 7
    if S < 3:
        print(0)
        return
    #dp[i][j] = i番目までの数の中で、合計がjになる組み合わせ数
    dp = [[0]*(S+1) for _ in range(S+1)]
    dp[0][0] = 1
    for i in range(1, S+1):
        for j in range(S+1):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % mod
            if j-i-1 >= 0:
                dp[i][j] -= dp[i-1][j-i-1]
                dp[i][j] %= mod
    print(dp[S][S])
