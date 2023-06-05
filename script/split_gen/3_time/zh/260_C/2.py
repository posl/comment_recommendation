def dfs(n, x, y):
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    ans = 1
    if n > 1:
        ans += dfs(n-1, x, y) + x
    if n > 2:
        for i in range(2, n):
            ans = min(ans, dfs(i, x, y) + dfs(n-i, x, y) + y)
    memo[n] = ans
    return ans
n, x, y = map(int, input().split())
memo = {}
print(dfs(n, x, y))
