Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    i, j = 0, 0
    for _ in range(H*W):
        if G[i][j] == "U":
            if i == 0:
                break
            else:
                i -= 1
        elif G[i][j] == "D":
            if i == H-1:
                break
            else:
                i += 1
        elif G[i][j] == "L":
            if j == 0:
                break
            else:
                j -= 1
        elif G[i][j] == "R":
            if j == W-1:
                break
            else:
                j += 1
    else:
        print(-1)
        return
    print(i+1, j+1)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    i, j = 0, 0
    for _ in range(H*W):
        if i == H-1 and j == W-1:
            break
        if grid[i][j] == "U":
            i -= 1
        elif grid[i][j] == "D":
            i += 1
        elif grid[i][j] == "L":
            j -= 1
        elif grid[i][j] == "R":
            j += 1
        if i < 0 or i >= H or j < 0 or j >= W:
            print(-1)
            return
    print(i+1, j+1)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    x = 0
    y = 0
    for i in range(10**6):
        if x == H-1 and y == W-1:
            print(x+1, y+1)
            return
        if G[x][y] == 'U' and x != 0:
            x -= 1
        elif G[x][y] == 'D' and x != H-1:
            x += 1
        elif G[x][y] == 'L' and y != 0:
            y -= 1
        elif G[x][y] == 'R' and y != W-1:
            y += 1
        else:
            print(-1)
            return
    print(-1)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    ans = [1, 1]
    for _ in range(H*W):
        i, j = ans[0]-1, ans[1]-1
        if G[i][j] == "U":
            if i == 0:
                break
            ans[0] -= 1
        elif G[i][j] == "D":
            if i == H-1:
                break
            ans[0] += 1
        elif G[i][j] == "L":
            if j == 0:
                break
            ans[1] -= 1
        elif G[i][j] == "R":
            if j == W-1:
                break
            ans[1] += 1
    else:
        ans = [-1]
    print(*ans)

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]

    sy, sx = 0, 0
    while True:
        if sy == h - 1 and sx == w - 1:
            print(sy + 1, sx + 1)
            return

        if grid[sy][sx] == 'U':
            sy -= 1
        elif grid[sy][sx] == 'D':
            sy += 1
        elif grid[sy][sx] == 'L':
            sx -= 1
        elif grid[sy][sx] == 'R':
            sx += 1

        if sy < 0 or sy >= h or sx < 0 or sx >= w:
            print(-1)
            return

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    s = [input() for _ in range(H)]
    x = 0
    y = 0
    c = 0
    while 1:
        c += 1
        if c > H * W:
            print(-1)
            break
        if s[y][x] == 'U':
            if y != 0:
                y -= 1
            else:
                print(y+1, x+1)
                break
        elif s[y][x] == 'D':
            if y != H - 1:
                y += 1
            else:
                print(y+1, x+1)
                break
        elif s[y][x] == 'L':
            if x != 0:
                x -= 1
            else:
                print(y+1, x+1)
                break
        elif s[y][x] == 'R':
            if x != W - 1:
                x += 1
            else:
                print(y+1, x+1)
                break

=======
Suggestion 7

def main():
    #入力
    h, w = map(int, input().split())
    g = [input() for _ in range(h)]
    #print(h, w)
    #print(g)
    #処理
    x = 0
    y = 0
    for i in range(10**5):
        if g[x][y] == "U":
            if x == 0:
                break
            else:
                x -= 1
        elif g[x][y] == "D":
            if x == h-1:
                break
            else:
                x += 1
        elif g[x][y] == "L":
            if y == 0:
                break
            else:
                y -= 1
        elif g[x][y] == "R":
            if y == w-1:
                break
            else:
                y += 1
        else:
            print("Error")
    else:
        print("-1")
        return
    #出力
    print(x+1, y+1)

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    grid = [input() for _ in range(h)]

    # 0:U, 1:D, 2:L, 3:R
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    d = [0, 1, 2, 3]

    # 0:U, 1:D, 2:L, 3:R
    d2c = ['U', 'D', 'L', 'R']

    # 0:U, 1:D, 2:L, 3:R
    d2i = {'U': 0, 'D': 1, 'L': 2, 'R': 3}

    x, y = 0, 0
    while True:
        c = grid[y][x]
        i = d2i[c]
        x += dx[i]
        y += dy[i]

        # 範囲外に出たら終了
        if x < 0 or x >= w or y < 0 or y >= h:
            break

        # 始点に戻ったら無限ループ
        if x == 0 and y == 0:
            print(-1)
            return

    print(y + 1, x + 1)

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]

    #print(H, W)
    #print(G)

    # すでに通った場所を記録する
    visited = [[False] * W for _ in range(H)]
    #print(visited)

    # 今いる場所
    i = 0
    j = 0

    # 移動回数
    cnt = 0

    # すでに通った場所かどうかを確認
    while not visited[i][j]:
        visited[i][j] = True
        cnt += 1
        #print(i, j)

        # 移動する
        if G[i][j] == 'U':
            i -= 1
        elif G[i][j] == 'D':
            i += 1
        elif G[i][j] == 'L':
            j -= 1
        elif G[i][j] == 'R':
            j += 1

        # 移動先がグリッドの範囲外ならば終了
        if i < 0 or i >= H or j < 0 or j >= W:
            break

    # 移動回数がグリッドのマス数より多ければ無限ループ
    if cnt > H * W:
        print(-1)
    else:
        print(i + 1, j + 1)

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    ans = [1, 1] #初期位置
    for i in range(1000000):
        if ans[0] == H and ans[1] == W:
            break
        if G[ans[0]-1][ans[1]-1] == 'U' and ans[0] != 1:
            ans[0] -= 1
        elif G[ans[0]-1][ans[1]-1] == 'D' and ans[0] != H:
            ans[0] += 1
        elif G[ans[0]-1][ans[1]-1] == 'L' and ans[1] != 1:
            ans[1] -= 1
        elif G[ans[0]-1][ans[1]-1] == 'R' and ans[1] != W:
            ans[1] += 1
        else:
            ans = [-1]
            break
    print(*ans)
