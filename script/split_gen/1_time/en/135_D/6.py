def main():
    S = input()
    N = len(S)
    mod = 10**9 + 7
    dp = [[0 for i in range(13)] for j in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        if S[i] == '?':
            for j in range(10):
                for k in range(13):
                    dp[i + 1][(k * 10 + j) % 13] += dp[i][k]
                    dp[i + 1][(k * 10 + j) % 13] %= mod
        else:
            j = int(S[i])
            for k in range(13):
                dp[i + 1][(k * 10 + j) % 13] += dp[i][k]
                dp[i + 1][(k * 10 + j) % 13] %= mod
    print(dp[N][5])
