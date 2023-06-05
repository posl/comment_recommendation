def dfs(start, parent, color):
    c = 1
    for to in edges[start]:
        if to == parent:
            continue
        if c == color:
            c += 1
        ans.append((start, to, c))
        dfs(to, start, c)
        c += 1
n = int(input())
edges = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
ans = []
dfs(1, 0, 0)
print(len(ans))
for a, b, c in ans:
    print(c)
