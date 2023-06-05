def dfs(x, y, t):
    global ans
    if x == n - 1:
        if t + a[y][0] == k:
            ans += 1
    else:
        for i in range(1, n):
            if not used[i]:
                used[i] = True
                dfs(x + 1, i, t + a[y][i])
                used[i] = False
n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
used = [False] * n
used[0] = True
ans = 0
dfs(0, 0, 0)
print(ans)
