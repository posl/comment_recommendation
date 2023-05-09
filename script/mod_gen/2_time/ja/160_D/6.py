def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    #グラフの初期化
    graph = [[0] * N for i in range(N)]
    #グラフの作成
    for i in range(N-1):
        graph[i][i+1] = 1
        graph[i+1][i] = 1
    graph[X][Y] = 1
    graph[Y][X] = 1
    #最短経路の探索
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][j] == 0 and graph[i][k] > 0 and graph[k][j] > 0:
                    graph[i][j] = graph[i][k] + graph[k][j]
    #距離ごとの整数の組の数の計算
    for k in range(1, N):
        count = 0
        for i in range(N):
            for j in range(i+1, N):
                if graph[i][j] == k:
                    count += 1
        print(count)

if __name__ == '__main__':
    main()