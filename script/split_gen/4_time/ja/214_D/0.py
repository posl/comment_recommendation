def main():
    N = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))
    #print(graph)
    # 1からの距離を求める
    from collections import deque
    dist = [float('inf')]*N
    dist[0] = 0
    q = deque([0])
    while q:
        u = q.popleft()
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                q.append(v)
    #print(dist)
    # 木の直径を求める
    dist2 = [float('inf')]*N
    dist2[0] = 0
    q = deque([0])
    while q:
        u = q.popleft()
        for v, w in graph[u]:
            if dist2[v] > dist2[u] + w:
                dist2[v] = dist2[u] + w
                q.append(v)
    #print(dist2)
    # 木の直径を求める
    dist3 = [float('inf')]*N
    dist3[0] = 0
    q = deque([0])
    while q:
        u = q.popleft()
        for v, w in graph[u]:
            if dist3[v] > dist3[u] + w:
                dist3[v] = dist3[u] + w
                q.append(v)
    #print(dist3)
    #print(sum(dist2))
    #print(sum(dist3))
    print(sum(dist2)+sum(dist3)-max(dist2))
