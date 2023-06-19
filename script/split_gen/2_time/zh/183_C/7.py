def dfs(i, k, n, t, visited):
    if k == 0 and visited == (1 << n) - 1:
        return 1
    ans = 0
    for j in range(n):
        if visited & (1 << j) == 0:
            ans += dfs(j, k - t[i][j], n, t, visited | (1 << j))
    return ans
n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
print(dfs(0, k, n, t, 1))
