def path():
    n,m = map(int, input().split())
    if m == 0:
        print("No")
        return
    #グラフ作成
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u,v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    #パス判定
    for i in range(n):
        if len(graph[i]) > 2:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    path()