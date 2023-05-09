def main():
    mod = 10 ** 9 + 7
    s = input()
    n = len(s)
    dp = [0] * 13
    dp[0] = 1
    for i in range(n):
        if s[i] == '?':
            ndp = [0] * 13
            for j in range(10):
                for k in range(13):
                    ndp[(k * 10 + j) % 13] += dp[k]
            dp = ndp
            dp = [i % mod for i in dp]
        else:
            ndp = [0] * 13
            for k in range(13):
                ndp[(k * 10 + int(s[i])) % 13] += dp[k]
            dp = ndp
    print(dp[5])
