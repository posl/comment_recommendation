def dfs(start, graph):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited
N, M, K = map(int, input().split())
friend = {i: set() for i in range(1, N+1)}
block = {i: set() for i in range(1, N+1)}
for _ in range(M):
    A, B = map(int, input().split())
    friend[A].add(B)
    friend[B].add(A)
for _ in range(K):
    C, D = map(int, input().split())
    block[C].add(D)
    block[D].add(C)
ans = [0] * N
for i in range(1, N+1):
    ans[i-1] = len(dfs(i, friend) - friend[i] - block[i] - {i}) - len(friend[i] & block[i])
print(*ans)
