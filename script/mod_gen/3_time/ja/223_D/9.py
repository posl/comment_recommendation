def main():
    #入力
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(M)]
    #グラフの初期化
    graph = [[] for _ in range(N+1)]
    in_degree = [0] * (N+1)
    #グラフの構築
    for a,b in AB:
        graph[a].append(b)
        in_degree[b] += 1
    #トポロジカルソート
    res = []
    que = []
    for i in range(1,N+1):
        if in_degree[i] == 0:
            que.append(i)
    while que:
        v = que.pop()
        res.append(v)
        for nv in graph[v]:
            in_degree[nv] -= 1
            if in_degree[nv] == 0:
                que.append(nv)
    #出力
    if len(res) != N:
        print(-1)
    else:
        print(*res)

if __name__ == '__main__':
    main()