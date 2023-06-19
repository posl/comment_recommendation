def solve(s):
    mod = 10 ** 9 + 7
    dp = [0] * 13
    dp[0] = 1
    for c in s:
        if c == '?':
            dp = [sum(dp[(j - k) % 13] for k in range(10)) % mod for j in range(13)]
        else:
            dp = [dp[(j - int(c)) % 13] for j in range(13)]
    return dp[5]
s = input()
print(solve(s))
