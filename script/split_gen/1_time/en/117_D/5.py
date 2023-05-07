def solve(N, K, A):
    A.sort(reverse=True)
    msb = 0
    while (1 << msb) <= K:
        msb += 1
    msb -= 1
    dp = [[0] * 2 for _ in range(msb + 1)]
    for i in range(msb + 1):
        dp[i][0] = dp[i][1] = 0
    for i in range(msb + 1):
        for j in range(N):
            if (A[j] >> i) & 1:
                dp[i][1] += 1
            else:
                dp[i][0] += 1
    ans = 0
    for i in range(msb + 1):
        if (K >> i) & 1:
            ans += (1 << i) * dp[i][0]
        else:
            ans += (1 << i) * dp[i][1]
    return ans
