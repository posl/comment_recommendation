def dfs(node, parent, color):
    c = 1
    for child in node:
        if child == parent:
            continue
        if c == color:
            c += 1
        ans[child] = c
        dfs(tree[child], node, c)
        c += 1
N = int(input())
tree = [[] for _ in range(N+1)]
ans = [0] * (N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
dfs(tree[1], 0, 0)
print(max(ans))
for i in range(2, N+1):
    print(ans[i])
