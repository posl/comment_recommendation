def main():
    n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    #print(n, x, y)
    graph = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    #print(graph)
    dist = [0]*n
    dist[x] = 0
    queue = [x]
    while queue:
        v = queue.pop(0)
        for u in graph[v]:
            if dist[u] != 0:
                continue
            dist[u] = dist[v] + 1
            queue.append(u)
    #print(dist)
    ans = [0]*n
    for i in range(n):
        ans[dist[i]] += 1
    for i in range(1, n):
        print(ans[i])
