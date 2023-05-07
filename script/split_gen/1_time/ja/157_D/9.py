def dfs(graph, start, goal):
    stack = [start]
    paths = []
    while stack:
        v = stack.pop()
        if v not in paths:
            paths.append(v)
            stack += graph[v]
    return paths
N, M, K = map(int, input().split())
friends = [[] for _ in range(N)]
blocks = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    friends[a-1].append(b)
    friends[b-1].append(a)
for _ in range(K):
    c, d = map(int, input().split())
    blocks[c-1].append(d)
    blocks[d-1].append(c)
ans = [0] * N
for i in range(N):
    ans[i] = len(set(dfs(friends, i+1, 0)) & set(dfs(blocks, i+1, 0))) - 1 - len(friends[i])
print(*ans)
