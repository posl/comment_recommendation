def main():
    N = int(input())
    E = [tuple(map(int, input().split())) for _ in range(N - 1)]
    G = [[] for _ in range(N)]
    for u, v, w in E:
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    # rootからの距離を求める
    dist = [0] * N
    dist[0] = 0
    stack = [0]
    while stack:
        u = stack.pop()
        for v, w in G[u]:
            if dist[v] == 0:
                dist[v] = dist[u] + w
                stack.append(v)
    # distの最大値と最小値を求める
    max_dist = max(dist)
    min_dist = min(dist)
    # distの最大値と最小値の差を求める
    diff = max_dist - min_dist
    # distの最大値と最小値の差を求める
    ans = diff * (N - 1) + sum(dist)
    print(ans)
