def main():
    N = int(input())
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    
    #print(X, Y)
    
    #グリッドの最大値
    MAX = 1000
    #グリッドの大きさ
    SIZE = MAX*2 + 1
    #グリッドの初期化
    grid = [[0]*SIZE for i in range(SIZE)]
    
    #グリッドに塗る
    for i in range(N):
        grid[X[i]+MAX][Y[i]+MAX] = 1
    
    #print(grid)
    
    #連結成分の数
    ans = 0
    #連結成分の探索
    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j] == 1:
                ans += 1
                dfs(i, j, grid)
    
    #print(grid)
    print(ans)

if __name__ == '__main__':
    main()