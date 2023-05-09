def main():
    N, X, Y = map(int, input().split())
    #グラフの作成
    G = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(i+1,N):
            if j == i+1 or (i+1 == X and j+1 == Y) or (i+1 == Y and j+1 == X):
                G[i][j] = 1
                G[j][i] = 1
    #print(G)
    #距離の計算
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if G[i][k] != 0 and G[k][j] != 0:
                    if G[i][j] == 0 or G[i][j] > G[i][k] + G[k][j]:
                        G[i][j] = G[i][k] + G[k][j]
    #print(G)
    #距離の数え上げ
    for k in range(1,N):
        count = 0
        for i in range(N):
            for j in range(i+1,N):
                if G[i][j] == k:
                    count += 1
        print(count)
