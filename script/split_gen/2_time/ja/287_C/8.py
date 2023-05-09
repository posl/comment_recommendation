def main():
    N, M = map(int, input().split())
    #print(N, M)
    #print("")
    #グラフの初期化
    graph = [[] for _ in range(N)]
    #グラフへの入力
    for i in range(M):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    #print(graph)
    #グラフの状態を確認
    for i in range(N):
        #print(graph[i])
        if graph[i] == []:
            print("No")
            return
    #パスグラフかどうか
    if N == M:
        print("Yes")
    else:
        print("No")
