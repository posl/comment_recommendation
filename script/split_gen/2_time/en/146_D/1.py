def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    # DFSで頂点の深さを求める
    d = [-1] * N
    q = [0]
    d[0] = 0
    while q:
        v = q.pop()
        for nv in G[v]:
            if d[nv] != -1:
                continue
            d[nv] = d[v] + 1
            q.append(nv)
    # 深い頂点から順に色を割り当てる
    color = [-1] * N
    q = [N-1]
    color[N-1] = 0
    while q:
        v = q.pop()
        c = 0
        for nv in G[v]:
            if d[nv] <= d[v]:
                continue
            if c == color[v]:
                c += 1
            color[nv] = c
            c += 1
            q.append(nv)
    print(max(color) + 1)
    for i in range(N-1):
        print(color[i]+1)
