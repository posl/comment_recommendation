def solve():
    n, s = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    dp = [[False for j in range(s+1)] for i in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(s+1):
            if dp[i][j]:
                dp[i+1][j] = True
                if j+a[i] <= s:
                    dp[i+1][j+a[i]] = True
                if j+b[i] <= s:
                    dp[i+1][j+b[i]] = True
    if not dp[n][s]:
        print('No')
        return
    print('Yes')
    ans = ['0' for i in range(n)]
    for i in range(n-1, -1, -1):
        if s-a[i] >= 0 and dp[i][s-a[i]]:
            ans[i] = 'A'
            s -= a[i]
        else:
            ans[i] = 'B'
            s -= b[i]
    print(''.join(ans))

if __name__ == '__main__':
    solve()