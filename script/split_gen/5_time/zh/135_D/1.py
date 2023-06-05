def main():
    s = input()
    mod = 10**9+7
    dp = [0]*13
    dp[0] = 1
    for c in s:
        if c == '?':
            dp = [sum(dp[4*i+j] for j in range(10))%mod for i in range(13)]
        else:
            dp = [dp[4*i+(10+int(c)-j)%10] for j in range(10)]
    print(dp[5])
