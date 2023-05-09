def main():
    N, S = map(int, input().split())
    a = []
    b = []
    for _ in range(N):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            dp[i + 1][j] = dp[i + 1][j] or dp[i][j]
            if j - a[i] >= 0:
                dp[i + 1][j] = dp[i + 1][j] or dp[i][j - a[i]]
            if j - b[i] >= 0:
                dp[i + 1][j] = dp[i + 1][j] or dp[i][j - b[i]]
    if dp[N][S]:
        print("Yes")
        ans = []
        for i in range(N):
            if S - a[N - i - 1] >= 0 and dp[N - i - 1][S - a[N - i - 1]]:
                ans.append("H")
                S -= a[N - i - 1]
            else:
                ans.append("T")
                S -= b[N - i - 1]
        print("".join(ans))
    else:
        print("No")
