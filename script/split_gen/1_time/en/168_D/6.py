def main():
    # Read data
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    # Create graph
    graph = [[] for _ in range(N+1)]
    for A, B in AB:
        graph[A].append(B)
        graph[B].append(A)
    # Create tree
    tree = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in graph[i]:
            if j != 1:
                tree[i].append(j)
    # Find the shortest path
    visited = [False] * (N+1)
    visited[1] = True
    queue = [(1, 1)]
    while queue:
        v, p = queue.pop(0)
        if v == 1:
            continue
        for w in tree[v]:
            if visited[w]:
                continue
            visited[w] = True
            queue.append((w, v))
    # Output
    print("Yes")
    for i in range(2, N+1):
        print(p)
