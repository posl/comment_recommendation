def main():
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n-1)]
    # print(data)
    # まずは頂点の最大値を求める
    max_v = 0
    for d in data:
        max_v = max(max_v, d[0], d[1])
    # print(max_v)
    # 隣接リストを作成する
    adj_list = [[] for _ in range(max_v)]
    for d in data:
        adj_list[d[0]-1].append([d[1]-1, d[2]])
        adj_list[d[1]-1].append([d[0]-1, d[2]])
    # print(adj_list)
    # ダイクストラ法で最短距離を求める
    # ここで、最短距離の値が最大となるものを求める
    # その最大値がf(i,j)となる
    import heapq
    INF = 10**18
    def dijkstra(s):
        dist = [INF] * max_v
        dist[s] = 0
        hq = [(0, s)] # (dist, vertex)
        heapq.heapify(hq)
        while hq:
            p = heapq.heappop(hq)
            v = p[1]
            if dist[v] < p[0]:
                continue
            for e in adj_list[v]:
                if dist[e[0]] > dist[v] + e[1]:
                    dist[e[0]] = dist[v] + e[1]
                    heapq.heappush(hq, (dist[e[0]], e[0]))
        return dist
    max_dist = 0
    for i in range(max_v):
        dist = dijkstra(i)
        for j in range(i+1, max_v):
            max_dist = max(max_dist, dist[j])
    print(max_dist * (n-1))

if __name__ == '__main__':
    main()