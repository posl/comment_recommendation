def main():
    #入力
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    #隣接リスト
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].append(b)
        adj[b].append(a)
    #Xからの距離
    dist = [-1]*N
    dist[X] = 0
    #Xからの距離が最も遠い頂点
    farthest = X
    #BFS
    que = [X]
    while que:
        v = que.pop()
        for nv in adj[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            que.append(nv)
            #Xからの距離が最も遠い頂点を更新
            if dist[nv] > dist[farthest]:
                farthest = nv
    #Yからの距離
    dist = [-1]*N
    dist[Y] = 0
    #BFS
    que = [Y]
    while que:
        v = que.pop()
        for nv in adj[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            que.append(nv)
    #Xからの距離が最も遠い頂点からYへの距離が最も遠い頂点までの距離を求める
    ans = 0
    for i in range(N):
        if i == farthest:
            continue
        if dist[i] > dist[farthest]:
            ans = max(ans, dist[i])
    print(ans)
