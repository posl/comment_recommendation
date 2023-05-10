def dfs(v, p, c):
    color = 1
    for u in tree[v]:
        if u == p:
            continue
        if color == c:
            color += 1
        ans[u] = color
        dfs(u, v, color)
        color += 1
n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
ans = [0] * n
ans[0] = 1
dfs(0, -1, 1)
print(max(ans))
for i in range(n-1):
    print(ans[i+1])
