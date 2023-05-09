def main():
    #入力
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(M)]
    #グラフの作成
    graph = [[] for _ in range(N)]
    for a,b in AB:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    #グラフの探索
    visited = [0]*N
    def dfs(v):
        visited[v] = 1
        for nv in graph[v]:
            if visited[nv] == 0:
                dfs(nv)
    dfs(0)
    #出力
    if 0 in visited:
        print('No')
    else:
        print('Yes')
