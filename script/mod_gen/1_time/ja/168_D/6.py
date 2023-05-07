def main():
    N, M = map(int, input().split())
    # 隣接リスト
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    # 部屋1から各部屋への最短距離
    dist = [float('inf')] * (N+1)
    dist[1] = 0
    # BFS
    q = [1]
    while q:
        v = q.pop(0)
        for nv in graph[v]:
            if dist[nv] == float('inf'):
                dist[nv] = dist[v] + 1
                q.append(nv)
    # 部屋1以外の部屋に道しるべを置く
    ans = [0] * (N+1)
    for i in range(2, N+1):
        for nv in graph[i]:
            if dist[nv] == dist[i] - 1:
                ans[i] = nv
                break
    # 出力
    print('Yes')
    for i in range(2, N+1):
        print(ans[i])
main()

if __name__ == '__main__':
    main()