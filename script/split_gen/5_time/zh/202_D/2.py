def main():
    A, B, K = map(int, input().split())
    # print(A, B, K)
    S = A + B
    dp = [[0 for j in range(S + 1)] for i in range(S + 1)]
    for i in range(S + 1):
        dp[i][0] = 1
        dp[i][i] = 1
    for i in range(1, S + 1):
        for j in range(1, S + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    # print(dp)
    ans = ""
    while A > 0 and B > 0:
        if K <= dp[A + B - 1][B]:
            ans += "a"
            A -= 1
        else:
            ans += "b"
            K -= dp[A + B - 1][B]
            B -= 1
    while A > 0:
        ans += "a"
        A -= 1
    while B > 0:
        ans += "b"
        B -= 1
    print(ans)
