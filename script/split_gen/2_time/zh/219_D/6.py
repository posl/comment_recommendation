def solve():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_, b_ = map(int, input().split())
        a.append(a_)
        b.append(b_)
    dp = [[[False for _ in range(301)] for _ in range(301)] for _ in range(n+1)]
    dp[0][0][0] = True
    for i in range(n):
        for j in range(x+1):
            for k in range(y+1):
                if dp[i][j][k]:
                    dp[i+1][j][k] = True
                    if j + a[i] <= x and k + b[i] <= y:
                        dp[i+1][j+a[i]][k+b[i]] = True
    ans = -1
    for i in range(1, n+1):
        if dp[i][x][y]:
            ans = i
            break
    print(ans)
