def main():
    N = int(input())
    uvw = [list(map(int, input().split())) for _ in range(N-1)]
    #print(N,uvw)
    # 隣接リストを作る
    g = [[] for _ in range(N)]
    for u, v, w in uvw:
        u -= 1
        v -= 1
        g[u].append((v, w))
        g[v].append((u, w))
    #print(g)
    # 0 からの距離を求める
    dist = [-1] * N
    dist[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv, w in g[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + w
            stack.append(nv)
    #print(dist)
    for i in range(N):
        if dist[i] % 2 == 0:
            print(0)
        else:
            print(1)

if __name__ == '__main__':
    main()