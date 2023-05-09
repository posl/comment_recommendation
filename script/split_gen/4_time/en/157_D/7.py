def dfs(start, goal):
    visited = [False] * (N+1)
    stack = []
    stack.append(start)
    while stack:
        node = stack.pop()
        if node == goal:
            return True
        if not visited[node]:
            visited[node] = True
            for i in range(len(graph[node])):
                if not visited[graph[node][i]]:
                    stack.append(graph[node][i])
    return False
N, M, K = map(int, input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(K):
    c, d = map(int, input().split())
    graph[c].append(d)
    graph[d].append(c)
for i in range(1, N+1):
    ans = 0
    for j in range(1, N+1):
        if i == j:
            continue
        if dfs(i, j):
            ans += 1
    print(ans, end = ' ')
