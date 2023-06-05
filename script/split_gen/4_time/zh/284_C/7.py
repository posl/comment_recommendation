def dfs(s):
    global u, v, n, used
    used[s] = True
    for i in range(n):
        if not used[i] and (u[i] == s or v[i] == s):
            dfs(i)
n, m = map(int, input().split())
u = [0] * m
v = [0] * m
used = [False] * n
for i in range(m):
    u[i], v[i] = map(int, input().split())
ans = 0
for i in range(n):
    if not used[i]:
        dfs(i)
        ans += 1
print(ans)
