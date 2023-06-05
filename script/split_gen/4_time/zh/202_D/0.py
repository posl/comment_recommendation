def solve(A, B, K):
    if A == 0:
        return 'b' * B
    if B == 0:
        return 'a' * A
    # dp[i][j]表示长度为i+j的字符串中，包含i个a和j个b的字符串的数量
    dp = [[0] * (B + 1) for _ in range(A + 1)]
    dp[0][0] = 1
    for i in range(A + 1):
        for j in range(B + 1):
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    # print(dp)
    ans = ''
    a, b = A, B
    for i in range(A + B):
        # print(a, b, dp[a - 1][b])
        if a > 0 and dp[a - 1][b] >= K:
            ans += 'a'
            a -= 1
        else:
            ans += 'b'
            K -= dp[a - 1][b]
            b -= 1
    return ans
A, B, K = map(int, input().split())
print(solve(A, B, K))
