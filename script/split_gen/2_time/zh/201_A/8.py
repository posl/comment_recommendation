def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a = [a[i] % 200 for i in range(n)]
    dp = [[-1 for _ in range(200)] for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(200):
            if dp[i][j] == -1:
                continue
            dp[i+1][j] = dp[i][j]
            dp[i+1][(j+a[i])%200] = i
    if dp[n][0] == 0:
        print("No")
        return
    print("Yes")
    ans = []
    i = n
    j = 0
    while i > 0:
        if dp[i][j] != dp[i-1][j]:
            ans.append(i)
            j = (j-a[i-1])%200
        i -= 1
    print(len(ans), *ans)
    ans = []
    i = n
    j = 0
    while i > 0:
        if dp[i][j] != dp[i-1][j]:
            ans.append(i)
            j = (j-a[i-1])%200
        i -= 1
    print(len(ans), *ans)
solve()
