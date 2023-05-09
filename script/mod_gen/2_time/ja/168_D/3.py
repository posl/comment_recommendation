def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    # 辺を追加するグラフ
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        graph[A[i]].append(B[i])
        graph[B[i]].append(A[i])
    
    # 部屋 1 からの距離を BFS で計算
    dist = [-1]*(N+1)
    dist[1] = 0
    q = [1]
    while len(q) > 0:
        v = q.pop(0)
        for nv in graph[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                q.append(nv)
    
    # 部屋 1 からの距離が最も遠い部屋を探す
    max_dist = 0
    max_dist_room = 0
    for i in range(1, N+1):
        if max_dist < dist[i]:
            max_dist = dist[i]
            max_dist_room = i
    
    # 部屋 1 からの距離が最も遠い部屋からの道しるべを辿る
    ans = [0]*(N+1)
    ans[max_dist_room] = 1
    for i in range(max_dist-1, -1, -1):
        for nv in graph[max_dist_room]:
            if dist[nv] == i:
                max_dist_room = nv
                ans[nv] = 1
                break
    
    # 出力
    print('Yes')
    for i in range(1, N+1):
        print(ans[i])

if __name__ == '__main__':
    main()