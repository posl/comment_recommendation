def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(lambda x: int(x) - 1, input().split())
        graph[A].append(B)
    # トポロジカルソート
    # 入次数を求める
    in_deg = [0] * N
    for i in range(N):
        for j in range(len(graph[i])):
            in_deg[graph[i][j]] += 1
    # 入次数0の頂点をキューに入れる
    que = []
    for i in range(N):
        if in_deg[i] == 0:
            que.append(i)
    # キューが空になるまで繰り返す
    ans = []
    while que:
        # キューから頂点を取り出す
        v = que.pop(0)
        ans.append(v)
        # 頂点vから出ている辺を削除
        for i in range(len(graph[v])):
            in_deg[graph[v][i]] -= 1
            # 新たに入次数0となった頂点をキューに入れる
            if in_deg[graph[v][i]] == 0:
                que.append(graph[v][i])
    if len(ans) != N:
        print(-1)
    else:
        print(*map(lambda x: x + 1, ans))

if __name__ == '__main__':
    main()