def main():
    n, m = map(int, input().split())
    a = []
    for i in range(m):
        a.append(list(map(int, input().split())))
    #print(n, m)
    #print(a)
    # グラフの作成
    graph = [[] for i in range(n)]
    for i in range(m):
        graph[a[i][0]-1].append(a[i][1]-1)
        graph[a[i][1]-1].append(a[i][0]-1)
    #print(graph)
    # 深さ優先探索
    def dfs(v):
        seen[v] = True
        for next_v in graph[v]:
            if seen[next_v]:
                continue
            dfs(next_v)
    # 連結成分の数を数える
    seen = [False] * n
    count = 0
    for v in range(n):
        if seen[v]:
            continue
        dfs(v)
        count += 1
    print(count)
