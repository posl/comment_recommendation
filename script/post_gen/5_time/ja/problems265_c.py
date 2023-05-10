Synthesizing 10/10 solutions

=======
Suggestion 1

def move(i, j, H, W):
    if i == H and j == W:
        return i, j
    if G[i][j] == "U" and i > 1:
        return move(i-1, j, H, W)
    if G[i][j] == "D" and i < H:
        return move(i+1, j, H, W)
    if G[i][j] == "L" and j > 1:
        return move(i, j-1, H, W)
    if G[i][j] == "R" and j < W:
        return move(i, j+1, H, W)
    return -1, -1

H, W = map(int, input().split())
G = [input() for _ in range(H)]
i, j = move(1, 1, H, W)
print(i, j)

=======
Suggestion 2

def move(i, j):
    if g[i][j] == 'U' and i > 0:
        return i-1, j
    elif g[i][j] == 'D' and i < H-1:
        return i+1, j
    elif g[i][j] == 'L' and j > 0:
        return i, j-1
    elif g[i][j] == 'R' and j < W-1:
        return i, j+1
    else:
        return i, j

H, W = map(int, input().split())
g = [list(input()) for _ in range(H)]
i, j = 0, 0
seen = [[False for _ in range(W)] for _ in range(H)]

while True:
    if seen[i][j]:
        print(-1)
        exit()
    seen[i][j] = True
    i, j = move(i, j)
    if i == H-1 and j == W-1:
        print(i+1, j+1)
        exit()

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    i = 0
    j = 0
    while True:
        if G[i][j] == 'U':
            if i == 0:
                print(i+1, j+1)
                break
            else:
                i -= 1
        elif G[i][j] == 'D':
            if i == H-1:
                print(i+1, j+1)
                break
            else:
                i += 1
        elif G[i][j] == 'L':
            if j == 0:
                print(i+1, j+1)
                break
            else:
                j -= 1
        elif G[i][j] == 'R':
            if j == W-1:
                print(i+1, j+1)
                break
            else:
                j += 1
        elif G[i][j] == '.':
            print(i+1, j+1)
            break
        else:
            print(-1)
            break

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    i, j = 0, 0
    while True:
        if G[i][j] == 'U':
            if i == 0:
                print(i+1, j+1)
                break
            else:
                i -= 1
        elif G[i][j] == 'D':
            if i == H-1:
                print(i+1, j+1)
                break
            else:
                i += 1
        elif G[i][j] == 'L':
            if j == 0:
                print(i+1, j+1)
                break
            else:
                j -= 1
        elif G[i][j] == 'R':
            if j == W-1:
                print(i+1, j+1)
                break
            else:
                j += 1
        if i == 0 and j == 0:
            print(-1)
            break

=======
Suggestion 5

def solve():
    H,W = map(int,input().split())
    G = [list(input()) for _ in range(H)]
    visited = [[False for _ in range(W)] for _ in range(H)]
    visited[0][0] = True
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    x = 0
    y = 0
    while True:
        if G[x][y] == 'U':
            x -= 1
        elif G[x][y] == 'D':
            x += 1
        elif G[x][y] == 'L':
            y -= 1
        elif G[x][y] == 'R':
            y += 1
        if x < 0 or H <= x or y < 0 or W <= y:
            print(x+1,y+1)
            return
        if visited[x][y]:
            print(-1)
            return
        visited[x][y] = True

=======
Suggestion 6

def main():
    # 標準入力の取得
    h, w = map(int, input().split())
    g = [list(input()) for i in range(h)]
    # print(h, w)
    # print(g)
    # 初期位置
    x = 0
    y = 0
    # 位置を保存
    pos = [[0 for i in range(w)] for j in range(h)]
    # print(pos)
    # 無限ループを検出するフラグ
    flag = 0
    # 無限ループを検出するためのカウンタ
    cnt = 0
    # 操作を繰り返す
    while True:
        # 次の位置を計算
        if g[x][y] == 'U':
            if x != 0:
                x -= 1
            else:
                flag = 1
        elif g[x][y] == 'D':
            if x != h - 1:
                x += 1
            else:
                flag = 1
        elif g[x][y] == 'L':
            if y != 0:
                y -= 1
            else:
                flag = 1
        elif g[x][y] == 'R':
            if y != w - 1:
                y += 1
            else:
                flag = 1
        # print(x, y)
        # 無限ループを検出した場合
        if flag == 1:
            break
        # 現在の位置に訪れた回数をカウント
        pos[x][y] += 1
        # print(pos)
        # 2回以上訪れた場合
        if pos[x][y] >= 2:
            flag = 2
            break
        # カウンタをインクリメント
        cnt += 1
        # print(cnt)
    # 結果を出力
    if flag == 1:
        print(-1)
    elif flag == 2:
        print(x + 1, y + 1)

=======
Suggestion 7

def main():
    H,W = map(int,input().split())
    G = [list(input()) for i in range(H)]
    #print(G)

    #print(G[0][0])
    #print(G[0][1])
    #print(G[1][0])
    #print(G[1][1])
    #print(G[0][1])

    #print(G[0][0])
    #print(G[0][1])
    #print(G[1][0])
    #print(G[1][1])
    #print(G[0][1])

    #print(G[0][0])
    #print(G[0][1])
    #print(G[1][0])
    #print(G[1][1])
    #print(G[0][1])

    #print(G[0][0])
    #print(G[0][1])
    #print(G[1][0])
    #print(G[1][1])
    #print(G[0][1])

    #print(G[0][0])
    #print(G[0][1])
    #print(G[1][0])
    #print(G[1][1])
    #print(G[0][1])
    #print(G[1][1])

    #print(G[0][0])
    #print(G[0][1])
    #print(G[1][0])
    #print(G[1][1])
    #print(G[0][1])
    #print(G[1][1])

    #print(G[0][0])
    #print(G[0][1])
    #print(G[1][0])
    #print(G[1][1])
    #print(G[0][1])
    #print(G[1][1])

    #print(G[0][0])
    #print(G[0][1])
    #print(G[1][0])
    #print(G[1][1])
    #print(G[0][1])
    #print(G[1][1])

    #print(G[0][0])
    #print(G[0][1])
    #print(G[1][0])
    #print(G[1][1])
    #print(G[0][1])
    #print(G[1][1])

    #print(G[0][0])
    #print(G[0][1])
    #

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    l = [list(input()) for _ in range(h)]
    x, y = 0, 0
    while True:
        if l[x][y] == "U":
            if x == 0:
                print(x+1, y+1)
                return
            else:
                x -= 1
        elif l[x][y] == "D":
            if x == h-1:
                print(x+1, y+1)
                return
            else:
                x += 1
        elif l[x][y] == "L":
            if y == 0:
                print(x+1, y+1)
                return
            else:
                y -= 1
        elif l[x][y] == "R":
            if y == w-1:
                print(x+1, y+1)
                return
            else:
                y += 1
        if l[x][y] == ".":
            print(x+1, y+1)
            return
        l[x][y] = "."
main()

=======
Suggestion 9

def main():
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    i = j = 0
    while True:
        if grid[i][j] == 'U':
            if i == 0:
                print(i+1, j+1)
                return
            else:
                i -= 1
        elif grid[i][j] == 'D':
            if i == h-1:
                print(i+1, j+1)
                return
            else:
                i += 1
        elif grid[i][j] == 'L':
            if j == 0:
                print(i+1, j+1)
                return
            else:
                j -= 1
        elif grid[i][j] == 'R':
            if j == w-1:
                print(i+1, j+1)
                return
            else:
                j += 1
        else:
            print(-1)
            return

=======
Suggestion 10

def solve():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]

    # 4方向の移動
    dx = [0, 1, 0, -1]  # 右,下,左,上
    dy = [1, 0, -1, 0]

    # スタート地点
    x, y = 0, 0

    # スタート地点の移動方向
    d = 0

    # 移動できるかどうか
    move = True

    # 移動できなくなるまで繰り返す
    while move:
        # 移動できるかどうかのフラグをFalseにしておく
        move = False

        # 移動方向に移動できるかどうか
        if 0 <= x + dx[d] < W and 0 <= y + dy[d] < H and G[y + dy[d]][x + dx[d]] != "#":
            x += dx[d]
            y += dy[d]
            move = True
        else:
            # 移動できなければ右に回転する
            d = (d + 1) % 4

    # 答えを出力
    print(y + 1, x + 1)
