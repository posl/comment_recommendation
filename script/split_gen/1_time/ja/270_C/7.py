def main():
    n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    # 隣接リスト
    E = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        E[u].append(v)
        E[v].append(u)
    # 各頂点からの距離を格納する配列
    dist = [0] * n
    # 頂点 x からの距離を求める
    q = [x]
    while q:
        v = q.pop()
        for u in E[v]:
            if dist[u] == 0:
                dist[u] = dist[v] + 1
                q.append(u)
    # 頂点 y からの距離を求める
    q = [y]
    while q:
        v = q.pop()
        for u in E[v]:
            if dist[u] == 0:
                dist[u] = dist[v] + 1
                q.append(u)
    # 各距離の頂点数を求める
    ans = [0] * n
    for d in dist:
        ans[d] += 1
    # 頂点 x と頂点 y の距離は 0 なので、それを除く
    print(*ans[1:])
