def solve(N, A):
    dp = [0] * (1 << 30)
    for a in A:
        dp[a] += 1
    for i in range(30):
        for j in range(1 << 30):
            if j & (1 << i):
                dp[j] += dp[j ^ (1 << i)]
    ans = 0
    for i in range(1 << 30):
        if dp[i] >= 2:
            ans |= i
    return ans
