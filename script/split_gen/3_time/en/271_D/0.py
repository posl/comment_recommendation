def main():
    n, s = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    dp = [[False for _ in range(s+1)] for _ in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(s+1):
            if j-a[i] >= 0 and dp[i][j-a[i]]:
                dp[i+1][j] = True
            if j-b[i] >= 0 and dp[i][j-b[i]]:
                dp[i+1][j] = True
    if not dp[n][s]:
        print("No")
        return
    print("Yes")
    ans = []
    for i in range(n, 0, -1):
        if s-a[i-1] >= 0 and dp[i-1][s-a[i-1]]:
            ans.append("H")
            s -= a[i-1]
        else:
            ans.append("T")
            s -= b[i-1]
    print("".join(ans[::-1]))
