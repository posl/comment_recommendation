def solve():
    n, s = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        a.append(tmp[0])
        b.append(tmp[1])
    dp = [[False for i in range(s+1)] for j in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(s+1):
            if j - a[i] >= 0 and dp[i][j-a[i]]:
                dp[i+1][j] = True
            elif j - b[i] >= 0 and dp[i][j-b[i]]:
                dp[i+1][j] = True
    if not dp[n][s]:
        print("No")
        return
    ans = [""] * n
    for i in range(n)[::-1]:
        if s - a[i] >= 0 and dp[i][s-a[i]]:
            s -= a[i]
            ans[i] = "H"
        else:
            s -= b[i]
            ans[i] = "T"
    print("Yes")
    print("".join(ans))

if __name__ == '__main__':
    solve()