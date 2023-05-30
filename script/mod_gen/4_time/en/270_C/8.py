def dfs(start, end, g):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in g[vertex] - set(path):
            if next == end:
                yield path + [next]
            else:
                stack.append((next, path + [next]))
N, X, Y = map(int, input().split())
g = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
print(len(list(dfs(X, Y, g))[0]) - 1)
