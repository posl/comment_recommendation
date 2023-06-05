def dfs(node, parent):
    global ans
    ans[node] += ans[parent]
    for child in tree[node]:
        if child != parent:
            dfs(child, node)
N, Q = map(int, input().split())
tree = [[] for _ in range(N+1)]
ans = [0] * (N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
for _ in range(Q):
    p, x = map(int, input().split())
    ans[p] += x
dfs(1, 0)
print(*ans[1:])
