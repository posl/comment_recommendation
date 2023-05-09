def main():
    S = input()
    S = S[::-1]
    mod = 10**9+7
    dp = [0]*13
    dp[0] = 1
    for i in range(len(S)):
        if S[i] == '?':
            ndp = [0]*13
            for j in range(10):
                for k in range(13):
                    ndp[(k*10+j)%13] += dp[k]
            dp = ndp
        else:
            ndp = [0]*13
            for j in range(13):
                ndp[(j*10+int(S[i]))%13] = dp[j]
            dp = ndp
        for j in range(13):
            dp[j] %= mod
    print(dp[5])
