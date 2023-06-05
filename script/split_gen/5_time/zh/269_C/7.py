def solve(n):
    if n == 0:
        return [0]
    ans = []
    def dfs(x, k):
        if x > n:
            return
        ans.append(x)
        if k == 60:
            return
        dfs(x * 2, k + 1)
        dfs(x * 2 + 1, k + 1)
    dfs(0, 0)
    return sorted(ans)
n = int(input())
ans = solve(n)
for x in ans:
    print(x)
