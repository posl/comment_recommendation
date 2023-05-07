def main():
    N = int(input())
    G = [[] for _ in range(10)]
    for _ in range(N):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    P = list(map(int, input().split()))
    P.insert(0, 0)
    # 頂点 1 から頂点 i への最短経路を求める
    dist = [float("inf")] * 10
    dist[1] = 0
    que = [1]
    while que:
        u = que.pop(0)
        for v in G[u]:
            if dist[v] == float("inf"):
                dist[v] = dist[u] + 1
                que.append(v)
    # 頂点 1 から頂点 i への最短経路の長さが偶数ならば、
    # コマ i を頂点 1 に移動させることで、最終的に頂点 i に移動させることができる
    ans = 0
    for i in range(1, 9):
        if dist[P[i]] % 2 == 0:
            ans += 1
    print(ans)
