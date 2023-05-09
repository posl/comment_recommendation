def main():
    n,m = map(int,input().split())
    if m == 0:
        print(0)
        return
    # 隣接リスト
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    # 1からNへの最短経路
    dist = [float('inf')]*n
    dist[0] = 0
    # 1からNへの最短経路の数
    count = [0]*n
    count[0] = 1
    # 幅優先探索
    q = [0]
    while q:
        v = q.pop(0)
        d = dist[v]
        for nv in adj[v]:
            if dist[nv] > d+1:
                dist[nv] = d+1
                count[nv] = count[v]
                q.append(nv)
            elif dist[nv] == d+1:
                count[nv] += count[v]
                count[nv] %= 10**9+7
    print(count[-1])
