def solve():
    A, B, K = map(int, input().split())
    n = A + B
    dp = [[0] * (B + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(B + 1):
            if j < B:
                dp[i + 1][j + 1] += dp[i][j]
            if j > 0:
                dp[i + 1][j - 1] += dp[i][j]
    ans = ""
    while A + B > 0:
        if A > 0:
            tmp = dp[A + B - 1][B]
            if tmp >= K:
                ans += "a"
                A -= 1
            else:
                ans += "b"
                B -= 1
                K -= tmp
        else:
            ans += "b"
            B -= 1
    print(ans)
