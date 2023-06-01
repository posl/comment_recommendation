Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                cnt = 1
                for k in range(j+1,W):
                    if S[i][k] == ".":
                        cnt += 1
                    else:
                        break
                for k in range(j-1,-1,-1):
                    if S[i][k] == ".":
                        cnt += 1
                    else:
                        break
                for k in range(i+1,H):
                    if S[k][j] == ".":
                        cnt += 1
                    else:
                        break
                for k in range(i-1,-1,-1):
                    if S[k][j] == ".":
                        cnt += 1
                    else:
                        break
                ans = max(ans,cnt)
    print(ans-3)

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            t = 0
            k = i
            while k >= 0 and s[k][j] == '.':
                t += 1
                k -= 1
            k = i
            while k < h and s[k][j] == '.':
                t += 1
                k += 1
            k = j
            while k >= 0 and s[i][k] == '.':
                t += 1
                k -= 1
            k = j
            while k < w and s[i][k] == '.':
                t += 1
                k += 1
            t -= 3
            ans = max(ans, t)
    print(ans)

=======
Suggestion 3

def main():
    h,w = map(int,input().split())
    s = [input() for _ in range(h)]
    #print(s)
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            cnt = 0
            for k in range(i-1,-1,-1):
                if s[k][j] == '#':
                    break
                cnt += 1
            for k in range(i+1,h):
                if s[k][j] == '#':
                    break
                cnt += 1
            for k in range(j-1,-1,-1):
                if s[i][k] == '#':
                    break
                cnt += 1
            for k in range(j+1,w):
                if s[i][k] == '#':
                    break
                cnt += 1
            ans = max(ans,cnt)
    print(ans+1)

=======
Suggestion 4

def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    # 各行各列的障碍物数
    row = [0] * H
    col = [0] * W
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                row[i] += 1
                col[j] += 1

    # 各行各列的障碍物数的最大值
    max_row = max(row)
    max_col = max(col)

    # 最大值的行数和列数
    row_num = row.count(max_row)
    col_num = col.count(max_col)

    # 最大值的行数和列数的交叉点
    # 交叉点上有障碍物则最大值减一
    cross = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#' and row[i] == max_row and col[j] == max_col:
                cross = 1

    print(max_row + max_col - cross)

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    print(S)
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                cnt = 0
                for k in range(i - 1, -1, -1):
                    if S[k][j] == '#':
                        break
                    cnt += 1
                for k in range(i + 1, H):
                    if S[k][j] == '#':
                        break
                    cnt += 1
                for k in range(j - 1, -1, -1):
                    if S[i][k] == '#':
                        break
                    cnt += 1
                for k in range(j + 1, W):
                    if S[i][k] == '#':
                        break
                    cnt += 1
                ans = max(ans, cnt + 1)
    print(ans)

=======
Suggestion 6

def main():
    h,w = map(int,input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            tmp = 0
            for k in range(i-1,-1,-1):
                if s[k][j] == '#':
                    break
                tmp += 1
            for k in range(i+1,h):
                if s[k][j] == '#':
                    break
                tmp += 1
            for k in range(j-1,-1,-1):
                if s[i][k] == '#':
                    break
                tmp += 1
            for k in range(j+1,w):
                if s[i][k] == '#':
                    break
                tmp += 1
            ans = max(ans,tmp)
    print(ans + 1)

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]

    # 縦方向に障害物があるかどうかを判定
    # あるならその位置までの距離を記録
    # ないなら-1を記録
    # dp[i][j] = (i, j)から上方向にある障害物までの距離
    dp = [[0] * W for i in range(H)]
    for j in range(W):
        for i in range(H):
            if S[i][j] == "#":
                dp[i][j] = -1
            elif i > 0:
                dp[i][j] = dp[i - 1][j] + 1

    # 横方向に障害物があるかどうかを判定
    # あるならその位置までの距離を記録
    # ないなら-1を記録
    # dp[i][j] = (i, j)から左方向にある障害物までの距離
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                dp[i][j] = -1
            elif j > 0:
                dp[i][j] += dp[i][j - 1]

    # 縦方向に障害物があるかどうかを判定
    # あるならその位置までの距離を記録
    # ないなら-1を記録
    # dp[i][j] = (i, j)から下方向にある障害物までの距離
    for j in range(W):
        for i in range(H - 1, -1, -1):
            if S[i][j] == "#":
                dp[i][j] = -1
            elif i < H - 1:
                dp[i][j] += dp[i + 1][

=======
Suggestion 8

def read():
    line = input()
    return line

=======
Suggestion 9

def get_lighted_cells(wall, H, W, i, j):
    lighted_cells = 0
    for k in range(i, H):
        if wall[k][j] == '#':
            break
        lighted_cells += 1
    for k in range(i, -1, -1):
        if wall[k][j] == '#':
            break
        lighted_cells += 1
    for k in range(j, W):
        if wall[i][k] == '#':
            break
        lighted_cells += 1
    for k in range(j, -1, -1):
        if wall[i][k] == '#':
            break
        lighted_cells += 1
    return lighted_cells - 3

=======
Suggestion 10

def light_num(H, W, S):
    light = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            else:
                light += 1
                k = i + 1
                while k < H:
                    if S[k][j] == '.':
                        light += 1
                    else:
                        break
                    k += 1
                k = i - 1
                while k >= 0:
                    if S[k][j] == '.':
                        light += 1
                    else:
                        break
                    k -= 1
                k = j + 1
                while k < W:
                    if S[i][k] == '.':
                        light += 1
                    else:
                        break
                    k += 1
                k = j - 1
                while k >= 0:
                    if S[i][k] == '.':
                        light += 1
                    else:
                        break
                    k -= 1
    return light
