Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    print(solve(n, x, y))

=======
Suggestion 2

def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    print(N - len(set(X)) - len(set(Y)) + 1)

=======
Suggestion 3

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

=======
Suggestion 4

def main():
    # 入力
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]

    # 処理
    ans = 0

    # 出力
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    B = []
    for i in range(N):
        B.append([A[i][0], A[i][1]])
        B.append([A[i][0]-1, A[i][1]])
        B.append([A[i][0], A[i][1]-1])
        B.append([A[i][0]+1, A[i][1]-1])
        B.append([A[i][0]-1, A[i][1]+1])
        B.append([A[i][0]+1, A[i][1]])
    B = set(map(tuple, B))
    B = list(B)
    B.sort()
    B = list(map(list, B))
    #print(B)
    #print(len(B))
    def union_find(n):
        par = [i for i in range(n)]
        rank = [0 for i in range(n)]
        def find(x):
            if par[x] == x:
                return x
            else:
                par[x] = find(par[x])
                return par[x]
        def same(x, y):
            return find(x) == find(y)
        def unite(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return False
            elif rank[x] < rank[y]:
                par[x] = y
            else:
                par[y] = x
                if rank[x] == rank[y]:
                    rank[x] += 1
            return True
        return find, same, unite
    find, same, unite = union_find(len(B))
    for i in range(len(B)):
        for j in range(i+1, len(B)):
            if B[i][0] == B[j][0] and B[i][1] == B[j][1]+1:
                unite(i, j)
            if B[i][0] == B[j][0]+1 and B[i][1] == B[j][1]:
                unite(i, j)
            if B[i][0] == B[j][0]+1 and B[i][1] == B[j][1]+1:
                unite(i, j)
            if B[i][0] == B[j][0]+1 and B[i][1] == B[j][1]-1:
                unite(i, j

=======
Suggestion 6

def main():
    N = int(input())
    XY = [list(map(int, input().split())) for i in range(N)]
    print(solve(N, XY))

=======
Suggestion 7

def main():
    N = int(input())
    XY = [list(map(int,input().split())) for i in range(N)]
    print(N)

=======
Suggestion 8

def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    #print(XY)
    XY.sort()
    #print(XY)
    #print(XY[0][0])
    #print(XY[0][1])
    #print(XY[0][0] + XY[0][1])
    #print(XY[1][0] + XY[1][1])
    #print(XY[2][0] + XY[2][1])
    #print(XY[3][0] + XY[3][1])
    #print(XY[4][0] + XY[4][1])
    #print(XY[5][0] + XY[5][1])
    #print(XY[6][0] + XY[6][1])
    #print(XY[7][0] + XY[7][1])
    #print(XY[8][0] + XY[8][1])
    #print(XY[9][0] + XY[9][1])
    #print(XY[10][0] + XY[10][1])
    #print(XY[11][0] + XY[11][1])
    #print(XY[12][0] + XY[12][1])
    #print(XY[13][0] + XY[13][1])
    #print(XY[14][0] + XY[14][1])
    #print(XY[15][0] + XY[15][1])
    #print(XY[16][0] + XY[16][1])
    #print(XY[17][0] + XY[17][1])
    #print(XY[18][0] + XY[18][1])
    #print(XY[19][0] + XY[19][1])
    #print(XY[20][0] + XY[20][1])
    #print(XY[21][0] + XY[21][1])
    #print(XY[22][0] + XY[22][1])
    #print(XY[23][0] + XY[23][1])
    #print(XY[24][0] + XY[24][1])
    #print(XY[25][0] + XY[

=======
Suggestion 9

def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]

    # マスの座標をグループ化
    XY_group = {}
    for x, y in XY:
        if x not in XY_group:
            XY_group[x] = [y]
        else:
            XY_group[x].append(y)

    # グループの中の座標をソート
    for x in XY_group:
        XY_group[x].sort()

    # グループの座標を繋げる
    for x in XY_group:
        for i in range(len(XY_group[x])-1):
            XY.append([x, XY_group[x][i]+1])

    # グループの座標を繋げる
    for x in XY_group:
        for i in range(len(XY_group[x])-1):
            XY.append([x, XY_group[x][i]-1])

    # グループの座標を繋げる
    for x in XY_group:
        for i in range(len(XY_group[x])):
            XY.append([x+1, XY_group[x][i]])
            XY.append([x-1, XY_group[x][i]])
            XY.append([x+1, XY_group[x][i]+1])
            XY.append([x-1, XY_group[x][i]-1])

    # グループの座標を繋げる
    for x in XY_group:
        for i in range(len(XY_group[x])-1):
            XY.append([x+1, XY_group[x][i]+1])
            XY.append([x-1, XY_group[x][i]-1])

    # グループの座標を繋げる
    for x in XY_group:
        for i in range(len(XY_group[x])-1):
            XY.append([x+1, XY_group[x][i]-1])
            XY.append([x-1, XY_group[x][i]+1])

    # グループの座標を繋げる
    for x in XY

=======
Suggestion 10

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
