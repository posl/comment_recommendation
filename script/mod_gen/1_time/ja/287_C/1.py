def main():
    #入力
    N, M = map(int, input().split())
    u = [0] * M
    v = [0] * M
    for i in range(M):
        u[i], v[i] = map(int, input().split())
    #処理
    #グラフの隣接リストを作成
    graph = [[] for i in range(N)]
    for i in range(M):
        graph[u[i] - 1].append(v[i] - 1)
        graph[v[i] - 1].append(u[i] - 1)
    #print(graph)
    #2頂点を選んで、その間の距離が1以外の辺が存在する場合はNoとする
    for i in range(N):
        for j in range(i + 2, N):
            #print(i, j)
            if j - i == 1:
                continue
            #print(i, j, graph[i], graph[j])
            if j in graph[i]:
                print("No")
                return
    print("Yes")
    return

if __name__ == '__main__':
    main()