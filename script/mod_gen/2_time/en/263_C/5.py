def dfs(n, m, depth, s):
    if depth == n:
        print(*s)
        return
    for i in range(1, m+1):
        if not s or s[-1] < i:
            s.append(i)
            dfs(n, m, depth+1, s)
            s.pop()
n, m = map(int, input().split())
dfs(n, m, 0, [])
