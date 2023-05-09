def main():
    # 入力
    N, M = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(M)]
    # グラフの初期化
    graph = [[] for _ in range(N + 1)]
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
    # 深さ優先探索
    seen = [0] * (N + 1)
    def dfs(v):
        seen[v] = 1
        for nv in graph[v]:
            if seen[nv] == 0:
                dfs(nv)
    # 連結成分の個数を数える
    ans = 0
    for i in range(1, N + 1):
        if seen[i] == 0:
            dfs(i)
            ans += 1
    # 出力
    print(ans)

if __name__ == '__main__':
    main()