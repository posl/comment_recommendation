def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(lambda x: int(x) - 1, input().split())
        G[u].append(v)
        G[v].append(u)
    # 二部グラフ判定
    color = [-1] * N
    color[0] = 0
    q = [0]
    while q:
        u = q.pop()
        for v in G[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                q.append(v)
    # 二部グラフならば、色が異なる頂点同士の辺の個数を数える
    if all(color[v] != -1 for v in range(N)):
        ans = sum(len(G[u]) for u in range(N)) // 2
        for u in range(N):
            for v in G[u]:
                if color[u] == color[v]:
                    ans -= 1
        ans //= 2
        print(ans)
    else:
        print(N * (N - 1) // 2 - M)

if __name__ == '__main__':
    main()