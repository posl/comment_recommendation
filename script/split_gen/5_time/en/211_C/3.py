def main():
    s = input()
    c = 'chokudai'
    dp = [0] * (len(c) + 1)
    dp[0] = 1
    mod = 10**9 + 7
    for i in range(len(s)):
        for j in range(len(c)):
            if s[i] == c[j]:
                dp[j+1] += dp[j]
                dp[j+1] %= mod
    print(dp[-1])
