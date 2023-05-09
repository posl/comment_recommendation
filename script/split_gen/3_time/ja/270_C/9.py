def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    #グラフを生成
    graph = [ [] for _ in range(N) ]
    for i in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    #XからYへの単純パスを列挙
    path = []
    path = dfs(graph, X, Y, path)
    #pathを出力
    for i in range(len(path)):
        if i == 0:
            print(path[i]+1, end="")
        else:
            print(" ", path[i]+1, sep="", end="")
    print()
