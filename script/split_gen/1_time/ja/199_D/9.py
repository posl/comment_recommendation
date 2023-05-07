def main():
    #入力
    N, M = map(int, input().split())
    #フラグ
    flag = 0
    #グラフの辺を格納するリスト
    graph = []
    #グラフの辺を格納
    for i in range(M):
        a, b = map(int, input().split())
        graph.append([a, b])
    #グラフの辺を格納したリストの要素数分ループ
    for i in range(M):
        if graph[i][0] == graph[i][1]:
            flag = 1
            break
    #グラフの辺を格納したリストの要素数分ループ
    for i in range(M):
        #グラフの辺を格納したリストの要素数分ループ
        for j in range(M):
            if graph[i][0] == graph[j][0] and graph[i][1] == graph[j][1]:
                flag = 1
                break
    #フラグが立っている場合
    if flag == 1:
        print(0)
    #フラグが立っていない場合
    else:
        print(3 ** N - 2 ** M)
