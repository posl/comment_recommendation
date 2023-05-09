def main():
    #入力
    M = int(input())
    edges = [list(map(int, input().split())) for _ in range(M)]
    p = list(map(int, input().split()))
    #グラフを作成
    graph = [[] for _ in range(9)]
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    #初期状態からの距離を求める
    dist = [9] * 9
    dist[0] = 0
    queue = [0]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if dist[w] == 9:
                dist[w] = dist[v] + 1
                queue.append(w)
    #頂点0からの距離が偶数の頂点にコマがあれば、それを頂点0に移動させる
    ans = 0
    for i in range(8):
        if dist[p[i]-1] % 2 == 0:
            ans += 1
    #頂点0からの距離が偶数の頂点が偶数なら、完成できる
    if ans % 2 == 0:
        print(ans)
    else:
        print(-1)

if __name__ == '__main__':
    main()