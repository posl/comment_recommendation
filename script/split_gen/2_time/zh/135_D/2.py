def main():
    s = input()
    l = len(s)
    dp = [0]*13
    dp[0] = 1
    for i in range(l):
        if s[i] == '?':
            dp1 = [0]*13
            for j in range(10):
                for k in range(13):
                    dp1[(k*10+j)%13] += dp[k]
            dp = dp1
            for j in range(13):
                dp[j] %= 1000000007
        else:
            dp1 = [0]*13
            for k in range(13):
                dp1[(k*10+int(s[i]))%13] += dp[k]
            dp = dp1
            for j in range(13):
                dp[j] %= 1000000007
    print(dp[5])
