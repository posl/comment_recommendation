Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            cnt = 0
            for k in range(i + 1, h):
                if s[k][j] == '#':
                    break
                cnt += 1
            for k in range(i - 1, -1, -1):
                if s[k][j] == '#':
                    break
                cnt += 1
            for k in range(j + 1, w):
                if s[i][k] == '#':
                    break
                cnt += 1
            for k in range(j - 1, -1, -1):
                if s[i][k] == '#':
                    break
                cnt += 1
            ans = max(ans, cnt + 1)
    print(ans)

=======
Suggestion 2

def get_max_light_num(h, w, s):
    # 从上往下，从左往右，第一个遇到的#号的位置
    top = [[0] * w for _ in range(h)]
    left = [[0] * w for _ in range(h)]
    # 从下往上，从右往左，第一个遇到的#号的位置
    bottom = [[0] * w for _ in range(h)]
    right = [[0] * w for _ in range(h)]

    # 从上往下，从左往右，第一个遇到的#号的位置
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                top[i][j] = i
                left[i][j] = j
            elif i > 0:
                top[i][j] = top[i-1][j]
                left[i][j] = left[i][j-1] if j > 0 else 0

    # 从下往上，从右往左，第一个遇到的#号的位置
    for i in range(h-1, -1, -1):
        for j in range(w-1, -1, -1):
            if s[i][j] == '#':
                bottom[i][j] = i
                right[i][j] = j
            elif i < h - 1:
                bottom[i][j] = bottom[i+1][j]
                right[i][j] = right[i][j+1] if j < w - 1 else w - 1

    # 计算灯光的照射范围
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            ans = max(ans, bottom[i][j] - top[i][j] + right[i][j] - left[i][j] + 1)
    return ans

=======
Suggestion 3

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

=======
Suggestion 4

def getLightNum(h,w,grid):
    #上下左右
    up = [0 for i in range(w)]
    down = [0 for i in range(w)]
    left = [0 for i in range(h)]
    right = [0 for i in range(h)]
    #上
    for i in range(w):
        if grid[0][i] == "#":
            up[i] = 0
        else:
            up[i] = 1
    #下
    for i in range(w):
        if grid[h-1][i] == "#":
            down[i] = 0
        else:
            down[i] = 1
    #左
    for i in range(h):
        if grid[i][0] == "#":
            left[i] = 0
        else:
            left[i] = 1
    #右
    for i in range(h):
        if grid[i][w-1] == "#":
            right[i] = 0
        else:
            right[i] = 1
    #print(up,down,left,right)
    #上
    for i in range(w):
        if up[i] == 1:
            for j in range(1,h):
                if grid[j][i] == "#":
                    break
                else:
                    up[i] += 1
    #下
    for i in range(w):
        if down[i] == 1:
            for j in range(h-2,-1,-1):
                if grid[j][i] == "#":
                    break
                else:
                    down[i] += 1
    #左
    for i in range(h):
        if left[i] == 1:
            for j in range(1,w):
                if grid[i][j] == "#":
                    break
                else:
                    left[i] += 1
    #右
    for i in range(h):
        if right[i] == 1:
            for j in range(w-2,-1,-1):
                if grid[i][j] == "#":
                    break
                else:
                    right[i] += 1
    #print(up,down,left,right)
    #求最大值
    max = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "#":

=======
Suggestion 5

def main():
    print('start')
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            t = 0
            for k in range(i - 1, -1, -1):
                if S[k][j] == '#':
                    break
                t += 1
            for k in range(i + 1, H):
                if S[k][j] == '#':
                    break
                t += 1
            for k in range(j - 1, -1, -1):
                if S[i][k] == '#':
                    break
                t += 1
            for k in range(j + 1, W):
                if S[i][k] == '#':
                    break
                t += 1
            ans = max(ans, t)
    print(ans + 1)

=======
Suggestion 6

def is_blocked(x, y, blocked):
    if x < 0 or x >= len(blocked[0]):
        return True
    if y < 0 or y >= len(blocked):
        return True
    return blocked[y][x]

=======
Suggestion 7

def print2D(s):
    for i in range(len(s)):
        print(s[i])
    print()

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # S[i][j] = 1 if S[i][j] == '.' else 0
    # dp[i][j] = (dp[i][j-1] if S[i][j-1] == '.' else 0) + (dp[i-1][j] if S[i-1][j] == '.' else 0) + (dp[i-1][j-1] if S[i-1][j-1] == '.' else 0) + S[i][j]
    dp = [[0 for _ in range(W)] for _ in range(H)]
    dp[0][0] = 1 if S[0][0] == '.' else 0
    for i in range(1, H):
        dp[i][0] = dp[i-1][0] if S[i-1][0] == '.' else 0
    for j in range(1, W):
        dp[0][j] = dp[0][j-1] if S[0][j-1] == '.' else 0
    for i in range(1, H):
        for j in range(1, W):
            dp[i][j] = (dp[i][j-1] if S[i][j-1] == '.' else 0) + (dp[i-1][j] if S[i-1][j] == '.' else 0) + (dp[i-1][j-1] if S[i-1][j-1] == '.' else 0) + (1 if S[i][j] == '.' else 0)
    print(dp[H-1][W-1])

=======
Suggestion 9

def main():
    #读取数据
    h,w = map(int,input().split())
    s = []
    for i in range(h):
        s.append(input())
    #print(s)

    #计算
    #每行的最左边的'#'到最右边的'#'的距离
    #每列的最上边的'#'到最下边的'#'的距离
    left = [[0]*w for i in range(h)]
    right = [[0]*w for i in range(h)]
    up = [[0]*w for i in range(h)]
    down = [[0]*w for i in range(h)]

    for i in range(h):
        for j in range(w):
            #print(i,j)
            if s[i][j] == '#':
                left[i][j] = 0
            else:
                if j == 0:
                    left[i][j] = 1
                else:
                    left[i][j] = left[i][j-1] + 1

    for i in range(h):
        for j in range(w-1,-1,-1):
            #print(i,j)
            if s[i][j] == '#':
                right[i][j] = 0
            else:
                if j == w-1:
                    right[i][j] = 1
                else:
                    right[i][j] = right[i][j+1] + 1

    for j in range(w):
        for i in range(h):
            #print(i,j)
            if s[i][j] == '#':
                up[i][j] = 0
            else:
                if i == 0:
                    up[i][j] = 1
                else:
                    up[i][j] = up[i-1][j] + 1

    for j in range(w):
        for i in range(h-1,-1,-1):
            #print(i,j)
            if s[i][j] == '#':
                down[i][j] = 0
            else:
                if i == h-1:
                    down[i][j] = 1
                else:
                    down[i][j] = down[i+1][j] + 1

    #print(left)
    #print(right)
    #print(up

=======
Suggestion 10

def main():
    pass
