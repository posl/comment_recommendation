def main():
    M = int(input())
    edges = [list(map(int, input().split())) for _ in range(M)]
    pieces = list(map(int, input().split()))
    # 連結成分の個数を調べる
    # 連結成分の個数が2以上なら、移動できない
    graph = [[] for _ in range(10)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * 10
    def dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:
                dfs(w)
    dfs(1)
    if not all(visited):
        print(-1)
        return
    # 連結成分の個数が1なら、移動回数は
    # 連結成分の頂点数から8を引いた数
    # 連結成分の頂点数が8以下なら、移動回数は0
    def count(v):
        visited[v] = True
        cnt = 1
        for w in graph[v]:
            if not visited[w]:
                cnt += count(w)
        return cnt
    visited = [False] * 10
    cnt = count(1)
    if cnt <= 8:
        print(0)
        return
    # 連結成分の個数が1なら、移動回数は
    # 連結成分の頂点数から8を引いた数
    # 連結成分の頂点数が8より大きいなら、移動回数は
    # 連結成分の頂点数から8を引いた数
    # 連結成分の頂点数が8より大きく、
    # 連結成分に頂点1が含まれていないなら、移動回数は-1
    if not visited[1]:
        print(-1)
        return
    # 連結成分の個数が1なら、移動回数

if __name__ == '__main__':
    main()