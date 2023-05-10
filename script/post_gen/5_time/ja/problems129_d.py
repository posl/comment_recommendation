Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H,W = map(int,input().split())
    S = [list(input()) for i in range(H)]
    #print(S)
    #print(S[0][0])
    #print(S[0][1])
    #print(S[0][2])
    #print(S[0][3])
    #print(S[0][4])
    #print(S[0][5])
    #print(S[0][6])
    #print(S[0][7])
    #print(S[0][8])
    #print(S[0][9])
    #print(S[0][10])
    #print(S[0][11])
    #print(S[0][12])
    #print(S[0][13])
    #print(S[0][14])
    #print(S[0][15])
    #print(S[0][16])
    #print(S[0][17])
    #print(S[0][18])
    #print(S[0][19])
    #print(S[0][20])
    #print(S[0][21])
    #print(S[0][22])
    #print(S[0][23])
    #print(S[0][24])
    #print(S[0][25])
    #print(S[0][26])
    #print(S[0][27])
    #print(S[0][28])
    #print(S[0][29])
    #print(S[0][30])
    #print(S[0][31])
    #print(S[0][32])
    #print(S[0][33])
    #print(S[0][34])
    #print(S[0][35])
    #print(S[0][36])
    #print(S[0][37])
    #print(S[0][38])
    #print(S[0][39])
    #print(S[0][40])
    #print(S[0][41])
    #print(S[0][42])
    #print(S[0][43])
    #print(S[0][44])
    #print(S[0][45])
    #print(S[0][46])
    #print(S[0][47])
    #print(S[0][48])
    #print(S[0][49])
    #print(S[0][50])
    #print(S[0][51])
    #

=======
Suggestion 2

def main():
    h,w = map(int,input().split())
    s = [input() for _ in range(h)]

    # #の数をカウント
    cnt = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                cnt += 1

    # 4方向に照らされるマス数をカウント
    # 4方向に照らされるマス数の最大値を求める
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            up = 0
            down = 0
            left = 0
            right = 0
            # 上方向
            for k in range(i,-1,-1):
                if s[k][j] == '#':
                    break
                up += 1
            # 下方向
            for k in range(i,h):
                if s[k][j] == '#':
                    break
                down += 1
            # 左方向
            for k in range(j,-1,-1):
                if s[i][k] == '#':
                    break
                left += 1
            # 右方向
            for k in range(j,w):
                if s[i][k] == '#':
                    break
                right += 1
            ans = max(ans,up+down+left+right-3)
    print(ans)

=======
Suggestion 3

def main():
    # H, W = map(int, input().split())
    # S = [list(input()) for _ in range(H)]
    H, W = 4, 6
    S = [
        ['#', '#', '.', '.', '#', '.'],
        ['.', '.', '.', '.', '.', '#'],
        ['.', '.', '.', '.', '#', '.'],
        ['#', '#', '.', '#', '.', '.']
    ]

    # まずは縦方向に照らされるマスを数える
    # その後、横方向に照らされるマスを数える
    # ちょっとややこしいので、縦方向のみを考える
    # そのために、縦方向の照らされるマスを数える関数を作る
    # その関数に、縦方向の照らされるマスを数える関数を渡す

    # 縦方向の照らされるマスを数える関数
    def count_light_v(S, H, W, x, y):
        count = 0
        # まずは上方向を数える
        for i in range(x, -1, -1):
            if S[i][y] == '#':
                break
            count += 1
        # 次に下方向を数える
        for i in range(x, H):
            if S[i][y] == '#':
                break
            count += 1
        return count

    # 横方向の照らされるマスを数える関数
    def count_light_h(S, H, W, x, y):
        count = 0
        # まずは左方向を数える
        for i in range(y, -1, -1):
            if S[x][i] == '#':
                break
            count += 1
        # 次に右方向を数える
        for i in range(y, W):
            if S[x][i] == '#':
                break
            count += 1
        return count

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    #print(s)
    #print(s[0][0])
    #print(s[1][0])
    #print(s[0][1])
    #print(s[1][1])
    #print(s[0][2])
    #print(s[1][2])
    #print(s[0][3])
    #print(s[1][3])
    #print(s[0][4])
    #print(s[1][4])
    #print(s[0][5])
    #print(s[1][5])
    #print(s[0][6])
    #print(s[1][6])
    #print(s[0][7])
    #print(s[1][7])
    #print(s[2][0])
    #print(s[3][0])
    #print(s[2][1])
    #print(s[3][1])
    #print(s[2][2])
    #print(s[3][2])
    #print(s[2][3])
    #print(s[3][3])
    #print(s[2][4])
    #print(s[3][4])
    #print(s[2][5])
    #print(s[3][5])
    #print(s[2][6])
    #print(s[3][6])
    #print(s[2][7])
    #print(s[3][7])
    ans = 0
    for i in range(h):
        for j in range(w):
            #print("i = %d, j = %d, s[i][j] = %s" % (i, j, s[i][j]))
            if s[i][j] == ".":
                #print("i = %d, j = %d, s[i][j] = %s" % (i, j, s[i][j]))
                #print("i = %d, j = %d, s[i][j] = %s" % (i, j, s[i][j]))
                #print("i = %d, j = %d, s[i][j] = %s" % (i, j, s[i][j]))
                #print("i = %d, j = %d, s

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                tmp = 0
                for k in range(j+1, W):
                    if S[i][k] == '.':
                        tmp += 1
                    else:
                        break
                for k in range(j-1, -1, -1):
                    if S[i][k] == '.':
                        tmp += 1
                    else:
                        break
                for k in range(i+1, H):
                    if S[k][j] == '.':
                        tmp += 1
                    else:
                        break
                for k in range(i-1, -1, -1):
                    if S[k][j] == '.':
                        tmp += 1
                    else:
                        break
                ans = max(ans, tmp+1)
    print(ans)

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]

    #print(H, W)
    #print(S)

    # まずは、左上から右下への斜めの線分について、障害物の存在を調べる
    # その後、右上から左下への斜めの線分について、障害物の存在を調べる
    # これらの両方の線分について、障害物の存在を調べることで、
    # 照らされるマスの個数を求めることができる

    # 全てのマスについて、左上から右下への斜めの線分について、障害物の存在を調べる
    # 左上から右下への斜めの線分について、障害物の存在を調べるために、
    # 左上から右下への斜めの線分の個数は、H + W - 1個ある
    # そのため、H + W - 1個の配列を作成し、それぞれの配列について、
    # 左上から右下への斜めの線分について、障害物の存在を調べる

    # 左上から右下への斜めの線分について、障害物の存在を調べるために、
    # 配列の左上から右下への斜めの線分の個数は、H + W - 1個ある
    # そのため、H + W - 1個の配列を作成し、それぞれの配列について、

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    #print(H, W)
    #print(S)
    #print(S[0][1])
    #print(S[1][1])
    #print(S[2][1])
    #print(S[3][1])

    #縦方向の光線
    #光線の始点を決める
    #光線が当たるマスを数える
    #光線の始点を変えて、光線が当たるマスを数える
    #最大値を求める
    #横方向の光線
    #光線の始点を決める
    #光線が当たるマスを数える
    #光線の始点を変えて、光線が当たるマスを数える
    #最大値を求める
    #縦方向の光線
    #光線の始点を決める
    #光線が当たるマスを数える
    #光線の始点を変えて、光線が当たるマスを数える
    #最大値を求める
    #横方向の光線
    #光線の始点を決める
    #光線が当たるマスを数える
    #光線の始点を変えて、光線が当たるマスを数える
    #最大値を求める
    #縦方向の光線
    #光線の始点を決める
    #光線が当たるマスを数える
    #光線の始点を変え

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '#':
                continue
            cnt = 0
            for dh, dw in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nh = h + dh
                nw = w + dw
                while 0 <= nh < H and 0 <= nw < W:
                    if S[nh][nw] == '#':
                        break
                    cnt += 1
                    nh += dh
                    nw += dw
            ans = max(ans, cnt)
    print(ans + 1)

=======
Suggestion 9

def main():
    # input
    H, W = map(int, input().split())
    Ss = [input() for _ in range(H)]

    # compute
    # dp[i][j] = (i, j) から右下に行くときの照らされるマスの最大値
    dp = [[0]*W for _ in range(H)]
    for i in range(H-1, -1, -1):
        for j in range(W-1, -1, -1):
            if Ss[i][j] == '#':
                continue
            if i == H-1 and j == W-1:
                dp[i][j] = 1
            elif i == H-1:
                dp[i][j] = dp[i][j+1] + 1
            elif j == W-1:
                dp[i][j] = dp[i+1][j] + 1
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1]) + 1

    # output
    print(dp[0][0])

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    #print(H, W)
    #print(S)
    #print(S[0][0])
    #print(S[0][1])
    #print(S[1][0])
    #print(S[1][1])
    #print(S[1][2])
    #print(S[2][1])
    #print(S[2][2])

    #print(S[0][0] == '.')
    #print(S[0][1] == '.')
    #print(S[1][0] == '.')
    #print(S[1][1] == '.')
    #print(S[1][2] == '.')
    #print(S[2][1] == '.')
    #print(S[2][2] == '.')

    #print(S[0][0] == '.' and S[0][1] == '.' and S[1][0] == '.' and S[1][1] == '.' and S[1][2] == '.' and S[2][1] == '.' and S[2][2] == '.')

    #print(S[0][0] == '.' and S[0][1] == '.' and S[1][0] == '.' and S[1][1] == '.' and S[1][2] == '.' and S[2][1] == '.' and S[2][2] == '.')

    #print(S[1][1] == '.' and S[1][2] == '.' and S[2][1] == '.' and S[2][2] == '.')

    #print(S[0][0] == '.' and S[0][1] == '.' and S[1][0] == '.' and S[1][1] == '.' and S[1][2] == '.' and S[2][1] == '.' and S[2][2] == '.' and S[2][3] == '.')

    #print(S[0][0] == '.' and S[0][1] == '.' and S[1][0] == '.' and S[1][1] == '.' and S[1][2] == '.' and S[2][1] == '.' and S[2][2] == '.' and S[2
