def main():
    S = input()
    mod = 10**9 + 7
    dp = [0] * 13
    dp[0] = 1
    for s in S:
        if s != '?':
            s = int(s)
            newdp = [0] * 13
            for i in range(13):
                newdp[(i * 10 + s) % 13] += dp[i]
            dp = newdp
        else:
            newdp = [0] * 13
            for i in range(13):
                for j in range(10):
                    newdp[(i * 10 + j) % 13] += dp[i]
            dp = newdp
        for i in range(13):
            dp[i] %= mod
    print(dp[5])
