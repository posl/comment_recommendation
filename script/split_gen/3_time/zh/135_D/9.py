def main():
    s = input()
    mod = 10**9+7
    dp = [0]*13
    dp[0] = 1
    for c in s:
        if c == "?":
            dp = [sum(dp[4*i+j] for j in range(13))%mod for i in range(10)]
        else:
            dp = [dp[4*i+(j-int(c))%13] for j in range(13)]
    print(dp[5])
