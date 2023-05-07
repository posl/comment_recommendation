def main():
    N, M = map(int, input().split())
    #print(N, M)
    #print("")
    #グラフの初期化
    graph = [[0]*N for i in range(N)]
    #print(graph)
    #print("")
    #グラフの作成
    for i in range(M):
        A_i, B_i = map(int, input().split())
        #print(A_i, B_i)
        graph[A_i-1][B_i-1] = 1
        graph[B_i-1][A_i-1] = 1
        #print(graph)
        #print("")
    #print(graph)
    #print("")
    #print(N, M)
    #print(graph)
    #print("")
    #頂点の色を決める
    color = [0]*N
    #print(color)
    #頂点の色を決める
    def dfs(v):
        #print("v", v)
        #print("color", color)
        #print("")
        #頂点の色を決める
        for c in range(3):
            #print("c", c)
            #print("")
            #頂点の色を決める
            color[v] = c
            #頂点の色を決める
            for i in range(N):
                #print("i", i)
                #print("")
                #頂点の色を決める
                if graph[v][i] == 1 and color[v] == color[i]:
                    #print("graph[v][i]", graph[v][i])
                    #print("color[v]", color[v])
                    #print("color[i]", color[i])
                    #print("")
                    #頂点の色を決める
                    return 0
            #頂点の色を決める
            if v+1 < N:
                #print("v+1", v+1)
                #print("")
                #頂点の色を決める
                if dfs(v+1) == 0:
                    #print("dfs(v+1)", dfs(v+1))
                    #print("")
                    #頂点の色を決める
