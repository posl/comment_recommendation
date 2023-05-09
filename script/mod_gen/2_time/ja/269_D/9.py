def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    #グリッドは無限に広いので、0,0を中心にN*2のグリッドを確保する
    grid = [[0 for _ in range(N*2)] for _ in range(N*2)]
    #黒く塗る
    for i in range(N):
        grid[XY[i][0]+N][XY[i][1]+N] = 1
    #連結成分の数を数える
    cnt = 0
    #探索済みのマスを記録する
    visited = [[0 for _ in range(N*2)] for _ in range(N*2)]
    for i in range(N*2):
        for j in range(N*2):
            #黒いマスかつ未訪問なら
            if grid[i][j] == 1 and visited[i][j] == 0:
                #連結成分を探索
                dfs(i, j, grid, visited)
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()