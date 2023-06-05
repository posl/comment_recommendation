def main():
    S = input()
    mod = 10**9+7
    dp = [[0 for _ in range(13)] for _ in range(len(S)+1)]
    dp[0][0] = 1
    for i in range(len(S)):
        for j in range(10):
            if S[i] != '?' and int(S[i]) != j:
                continue
            for k in range(13):
                dp[i+1][(k*10+j)%13] += dp[i][k]
                dp[i+1][(k*10+j)%13] %= mod
    print(dp[len(S)][5])
